from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Ticket, Pot

@login_required
def buy_tickets(request):
    if request.method == "POST":
        try:
            amount = int(request.POST.get("amount", 0))
            if amount <= 0:
                raise ValueError("Amount must be positive.")
            
            ticket = Ticket.objects.create(user=request.user, amount=amount)
            pot = Pot.objects.last() or Pot.objects.create()
            pot.total_amount += amount * 1000000  # 1 ticket = 1M ISK
            pot.save()
            messages.success(request, f"You successfully bought {amount} tickets!")
        except Exception as e:
            messages.error(request, f"Error: {e}")
        return redirect('buy_tickets')

    return render(request, "fortunaisk/buy_tickets.html", {"pot": Pot.objects.last()})
