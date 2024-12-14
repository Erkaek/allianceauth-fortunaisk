from django.urls import path
from allianceauth.services.hooks import MenuItemHook
from django.utils.translation import gettext_lazy as _
from . import views
import logging

logger = logging.getLogger(__name__)

app_name = 'fortunaisk'

# Hook pour le menu principal d'Alliance Auth
class RaffleMenu(MenuItemHook):
    def __init__(self):
        logger.debug("[DEBUG] Hook RaffleMenu enregistré pour FortunaISK.")
        super().__init__(
            _('FortunaISK'),  # Nom dans le menu
            'fortunaisk:main_view',  # Vue associée
            navactive=['fortunaisk']
        )

    def permissions(self, user):
        return user.has_perm('fortunaisk.view_raffle')  # Permission requise

MenuItemHook.register(RaffleMenu)

# Routes du module
urlpatterns = [
    path('', views.main_view, name='main_view'),
    path('history/', views.history_view, name='history_view'),
]
