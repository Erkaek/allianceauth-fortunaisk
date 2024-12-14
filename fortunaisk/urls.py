from django.urls import path
from allianceauth.services.hooks import MenuItemHook
from django.utils.translation import gettext_lazy as _
from . import views

app_name = 'fortunaisk'

# Hook pour le menu principal d'Alliance Auth
class RaffleMenu(MenuItemHook):
    def __init__(self):
        super().__init__(
            _('FortunaISK'),  # Nom affiché dans le menu
            'fortunaisk:main_view',  # Vue principale du module
            navactive=['fortunaisk']  # Activer l'entrée de menu pour toutes les vues du module
        )

    def permissions(self, user):
        return user.has_perm('fortunaisk.view_raffle')  # Permission requise

MenuItemHook.register(RaffleMenu)

# Routes internes du module
urlpatterns = [
    path('', views.main_view, name='main_view'),  # Vue principale
    path('history/', views.history_view, name='history_view'),  # Historique des gagnants
]
