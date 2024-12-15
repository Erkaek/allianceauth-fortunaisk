from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from .models import Ticket, Winner


@login_required
def tickets_list(request):
    """View for displaying the list of tickets."""
    tickets = Ticket.objects.filter(character__character_ownership__user=request.user)
    return render(request, 'fortunaisk/tickets.html', {'tickets': tickets})


@login_required
def winner_list(request):
    """View for displaying the list of winners."""
    winners = Winner.objects.all()
    return render(request, 'fortunaisk/winner.html', {'winners': winners})


@permission_required('fortunaisk.admin')
def admin_dashboard(request):
    """Admin dashboard for managing Fortunaisk."""
    return render(request, 'fortunaisk/admin.html')
