from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import RaffleTicket, RaffleWinner
from django.db.models import Sum
from django.utils import timezone
from allianceauth.characters.models import Character

@login_required
def main_view(request):
    """
    Vue principale du module FortunaISK.
    Affiche le pot total, les instructions, le statut de participation de l'utilisateur,
    le nombre total de tickets achetés, et la valeur d'un ticket.
    """
    # Récupérer la valeur du ticket définie en admin
    ticket_value = getattr(settings, 'FORTUNAISK_TICKET_VALUE', 1000)  # Default à 1000 ISK si non défini

    # Calculer le pot total en cours (pour le mois en cours)
    now = timezone.now()
    total_pot = RaffleTicket.objects.filter(
        purchase_date__year=now.year,
        purchase_date__month=now.month
    ).aggregate(total=Sum('price_isk'))['total'] or 0

    # Nombre total de tickets achetés
    total_tickets = RaffleTicket.objects.filter(
        purchase_date__year=now.year,
        purchase_date__month=now.month
    ).count()

    # Vérifier si l'utilisateur a une participation active via n'importe quel de ses personnages
    user_characters = Character.objects.filter(owner=request.user)
    has_active_participation = RaffleTicket.objects.filter(
        character__in=user_characters,
        purchase_date__year=now.year,
        purchase_date__month=now.month
    ).exists()

    context = {
        'total_pot': total_pot,
        'ticket_value': ticket_value,
        'total_tickets': total_tickets,
        'has_active_participation': has_active_participation,
    }

    return render(request, 'fortunaisk/main.html', context)

@login_required
def history_view(request):
    """
    Vue affichant l'historique des gagnants.
    """
    winners = RaffleWinner.objects.all().order_by('-draw_date')
    context = {
        'winners': winners,
    }
    return render(request, 'fortunaisk/history.html', context)
