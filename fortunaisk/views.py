from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import logging

logger = logging.getLogger(__name__)

@login_required
def main_view(request):
    """
    Main view for FortunaISK Lottery.
    """
    # Exemple de données de test
    jackpot = 10000000
    user_participation = True  # Modifier selon les conditions réelles

    # Log pour débogage
    logger.debug(f"Main View - Jackpot: {jackpot}, Participation: {user_participation}")

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
    # Exemple de données statiques pour l'historique des gagnants
    winners = [
        {"date": "2024-12-01", "winner": "John Doe", "jackpot": "10,000,000 ISK"},
        {"date": "2024-11-01", "winner": "Jane Smith", "jackpot": "8,000,000 ISK"},
    ]

    # Log pour débogage
    logger.debug(f"History View - Winners: {winners}")

    context = {
        "winners": winners,
    }

    return render(request, "fortunaisk/history.html", context)
