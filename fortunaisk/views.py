from django.shortcuts import render
from .models import Ticket, Winner

def ticket_list(request):
    tickets = Ticket.objects.all()
    return render(request, "fortunaisk/ticket.html", {"tickets": tickets})

def winner_list(request):
    winners = Winner.objects.all()
    return render(request, "fortunaisk/winner.html", {"winners": winners})
