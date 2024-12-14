from django.urls import path
from allianceauth.services.hooks import MenuItemHook
from django.utils.translation import gettext_lazy as _
from . import views

app_name = 'fortunaisk'

# Hook pour ajouter le module au menu principal d'Alliance Auth
class RaffleMenu(MenuItemHook):
    def __init__(self):
        super().__init__(
            _('FortunaISK'),  # Nom affiché dans le menu
            'fortunaisk:main_view',  # Nom de la vue principale
            navactive=['fortunaisk']  # Active l'entrée pour toutes les pages du module
        )

    def permissions(self, user):
        # Définir la permission requise pour afficher le module
        return user.has_perm('fortunaisk.view_raffle')

# Enregistrement du Hook
MenuItemHook.register(RaffleMenu)

# Définition des URLs du module
urlpatterns = [
    path('', views.main_view, name='main_view'),  # Vue principale
    path('history/', views.history_view, name='history_view'),  # Vue historique des gagnants
]
