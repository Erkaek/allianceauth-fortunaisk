from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import RaffleTicket, RaffleWinner
from django.db.models import Sum
from django.utils import timezone
from allianceauth.eveonline.models import EveCharacterOwnership


@login_required
def main_view(request):
    """
    Vue principale du module FortunaISK.
    """
    try:
        ticket_value = getattr(settings, 'FORTUNAISK_TICKET_VALUE', 1000)
        now = timezone.now()

        # Calculer le pot total pour le mois en cours
        total_pot = RaffleTicket.objects.filter(
            purchase_date__year=now.year,
            purchase_date__month=now.month
        ).aggregate(total=Sum('price_isk'))['total'] or 0

        # Nombre de tickets achetés pour le mois en cours
        total_tickets = RaffleTicket.objects.filter(
            purchase_date__year=now.year,
            purchase_date__month=now.month
        ).count()

        # Vérification de la participation active
        user_characters = EveCharacterOwnership.objects.filter(user=request.user).values_list('character', flat=True)
        has_active_participation = RaffleTicket.objects.filter(
            character__id__in=user_characters,
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

    except Exception as e:
        return render(request, 'fortunaisk/error.html', {'error': str(e)})


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
