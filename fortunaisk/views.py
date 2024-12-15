from django.shortcuts import render
from django.utils import timezone
from .models import Lottery

def current_lottery(request):
    lottery = Lottery.objects.filter(is_active=True, end_date__gte=timezone.now()).first()
    return render(request, 'fortunaisk/current_lottery.html', {'lottery': lottery})

def winners_history(request):
    past_lotteries = Lottery.objects.filter(is_active=False).order_by('-end_date')
    return render(request, 'fortunaisk/winners_history.html', {'past_lotteries': past_lotteries})
