from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def main_view(request):
    """
    Main view for FortunaISK Lottery.
    """
    # Exemple de données dynamiques
    jackpot = 10000000  # Montant du jackpot (par exemple)
    user_participation = True  # Indique si l'utilisateur participe à la loterie

    context = {
        "jackpot": jackpot,
        "user_participation": user_participation,
    }

    return render(request, "fortunaisk/main.html", context)


@login_required
def history_view(request):
    """
    View to display the history of lottery winners.
    """
    # Exemple de données statiques pour les tests
    winners = [
        {"date": "2024-12-01", "winner": "John Doe", "jackpot": "10,000,000 ISK"},
        {"date": "2024-11-01", "winner": "Jane Smith", "jackpot": "8,000,000 ISK"},
    ]

    context = {
        "winners": winners,
    }

    return render(request, "fortunaisk/history.html", context)
