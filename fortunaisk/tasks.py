from celery import shared_task
from .models import Ticket, Pot, Winner
import random
from django.utils.timezone import now
from .utils import notify_winner_discord

@shared_task
def draw_winner():
    pot = Pot.objects.last()
    if not pot or pot.total_amount == 0:
        return "No pot available for drawing."
    
    tickets = Ticket.objects.all()
    if not tickets.exists():
        return "No tickets sold."

    # Préparer la loterie
    ticket_pool = [(ticket.user, ticket.amount) for ticket in tickets]
    winner = random.choices(ticket_pool, weights=[x[1] for x in ticket_pool], k=1)[0]

    # Enregistrer le gagnant
    Winner.objects.create(user=winner[0], won_at=now(), amount_won=pot.total_amount)

    # Réinitialiser le pot
    pot.total_amount = 0
    pot.save()

    # Notification
    notify_winner_discord(winner[0], pot.total_amount)

    return f"Winner drawn: {winner[0].username}, Amount: {pot.total_amount} ISK"
