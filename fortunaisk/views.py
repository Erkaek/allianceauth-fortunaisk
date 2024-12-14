from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def main_view(request):
    """
    Main view for FortunaISK.
    """
    return render(request, 'fortunaisk/main.html')


@login_required
def history_view(request):
    """
    History view for past raffle winners.
    """
    return render(request, 'fortunaisk/history.html')
