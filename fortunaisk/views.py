from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def main_view(request):
    """
    Vue principale du module FortunaISK.
    """
    return render(request, 'fortunaisk/main.html')

@login_required
def history_view(request):
    """
    Vue pour afficher l'historique des gagnants.
    """
    return render(request, 'fortunaisk/history.html')
