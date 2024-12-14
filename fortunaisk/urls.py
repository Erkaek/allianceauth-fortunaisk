import logging
from django.urls import path
from allianceauth.services.hooks import MenuItemHook
from django.utils.translation import gettext_lazy as _
from . import views

# Configuration du logger
logger = logging.getLogger(__name__)

class RaffleMenu(MenuItemHook):
    def __init__(self):
        logger.debug("[DEBUG] Enregistrement du hook RaffleMenu.")
        super().__init__(
            _('Raffle'),
            'fortunaisk:main_view',
            navactive=['fortunaisk']
        )

    def permissions(self, user):
        logger.debug(f"[DEBUG] Vérification des permissions pour : {user.username}")
        return user.has_perm('fortunaisk.view_raffle')

MenuItemHook.register(RaffleMenu)

app_name = 'fortunaisk'

urlpatterns = [
    path('', views.main_view, name='main_view'),
    path('history/', views.history_view, name='history_view'),
]
