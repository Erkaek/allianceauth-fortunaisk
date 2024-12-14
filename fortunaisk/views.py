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
    View to display the history of lottery winners.
    """
    # Données statiques pour tester le rendu
    winners = [
        {"date": "2024-12-01", "winner": "John Doe", "jackpot": "10,000,000 ISK"},
        {"date": "2024-11-01", "winner": "Jane Smith", "jackpot": "8,000,000 ISK"},
    ]
    return render(request, 'fortunaisk/history.html', {'winners': winners})