# views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Ticket, Winner

@login_required
def index(request):
    tickets = Ticket.objects.filter(character__character_ownership__user=request.user)
    context = {'tickets': tickets}
    return render(request, 'fortunaisk/tickets.html', context)

@login_required
def winners(request):
    winners = Winner.objects.all().order_by('-won_at')
    context = {'winners': winners}
    return render(request, 'fortunaisk/winners.html', context)
