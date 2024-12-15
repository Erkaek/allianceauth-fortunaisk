from django.shortcuts import render
from .models import LotteryConfig, LotteryWinner

def index(request):
    config = LotteryConfig.objects.last()
    context = {
        'ticket_price': config.ticket_price if config else 0,
        'reference_id': config.reference_id if config else "No Reference",
        'corporation_id': config.corporation_id if config else 0,
    }
    return render(request, 'fortunaisk/index.html', context)

def winners(request):
    winners = LotteryWinner.objects.all().order_by('-date')
    return render(request, 'fortunaisk/winners.html', {'winners': winners})
