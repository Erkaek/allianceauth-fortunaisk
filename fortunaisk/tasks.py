import random
from django.utils import timezone
from .models import RaffleTicket, RaffleWinner
from django.conf import settings
import logging
from celery import shared_task
from allianceauth_invoices.models import Invoice
from allianceauth.characters.models import Character

logger = logging.getLogger(__name__)

@shared_task
def validate_fortunaisk_payments():
    """
    Vérifie les paiements pour FortunaISK en utilisant allianceauth-invoices.
    Crée des tickets pour les paiements valides qui n'ont pas encore été traités.
    """
    # Filtrer les invoices correspondant à FortunaISK qui sont payées et valides
    invoices = Invoice.objects.filter(
        reference__startswith=settings.INVOICE_REF_FORTUNAISK,  # Référence unique pour FortunaISK
        is_paid=True,
        is_valid=True
    )

    for invoice in invoices:
        # Vérifiez si un ticket a déjà été créé pour cette référence
        if not RaffleTicket.objects.filter(payment_reference=invoice.reference).exists():
            try:
                # Extraire le nom de l'utilisateur et du personnage de la référence
                # Format de référence : FORTUNAISK-username-charactername-YYYYMM
                parts = invoice.reference.split('-')
                if len(parts) < 4:
                    logger.error(f"Référence de paiement invalide : {invoice.reference}")
                    continue
                prefix, username, *character_parts, ym = parts
                character_name = '-'.join(character_parts)
                if prefix != settings.INVOICE_REF_FORTUNAISK:
                    logger.error(f"Préfixe de référence incorrect : {invoice.reference}")
                    continue

                user = invoice.user  # Supposant que Invoice a un ForeignKey vers User
                character = Character.objects.get(name=character_name, owner=user)

                # Créer un ticket
                RaffleTicket.objects.create(
                    character=character,
                    user=user,
                    price_isk=settings.FORTUNAISK_TICKET_VALUE,
                    payment_reference=invoice.reference
                )
                logger.info(f"Ticket créé pour l'utilisateur {user.username} avec le personnage {character.name} et la référence {invoice.reference}")
            except Character.DoesNotExist:
                logger.error(f"Personnage {character_name} pour l'utilisateur {username} non trouvé.")
            except Exception as e:
                logger.error(f"Erreur lors de la création du ticket pour la référence {invoice.reference} : {str(e)}")

@shared_task
def run_monthly_raffle():
    """
    Sélectionne un gagnant aléatoire parmi les tickets du mois en cours,
    enregistre le gagnant et le total dans RaffleWinner.
    Envoie une notification Discord via webhook.
    """
    now = timezone.now()
    # Filtrer les tickets du mois en cours
    month_tickets = RaffleTicket.objects.filter(
        purchase_date__year=now.year,
        purchase_date__month=now.month
    )

    if not month_tickets.exists():
        logger.info("Aucun ticket acheté ce mois-ci. Aucun tirage effectué.")
        return None  # Pas de tickets ce mois-ci, donc pas de gagnant

    total_pot = sum(ticket.price_isk for ticket in month_tickets)
    winner_ticket = random.choice(month_tickets)

    # Créer un enregistrement de gagnant
    winner_record = RaffleWinner.objects.create(
        user=winner_ticket.user,
        main_character=winner_ticket.character.name,
        total_pot=total_pot,
        draw_date=now
    )

    # Envoyer une notification Discord via webhook
    discord_webhook_url = getattr(settings, 'FORTUNAISK_DISCORD_WEBHOOK_URL', None)
    if discord_webhook_url:
        import requests
        data = {
            "content": f"🎉 Félicitations à **{winner_record.user.username}** (**{winner_record.main_character}**) pour avoir gagné **{winner_record.total_pot} ISK** ! 🎉"
        }
        response = requests.post(discord_webhook_url, json=data)
        if response.status_code not in [200, 204]:
            logger.error(f"Erreur lors de l'envoi de la notification Discord : {response.status_code} - {response.text}")
    else:
        logger.warning("URL de webhook Discord non configurée. Notification non envoyée.")

    logger.info(f"Gagnant du tirage {now.strftime('%Y-%m-%d')}: {winner_record.user.username} ({winner_record.main_character}) a gagné {total_pot} ISK.")
    return winner_record
