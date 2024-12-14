from allianceauth.services.hooks import MenuItemHook
from django.utils.translation import gettext_lazy as _
from django.urls import path
from . import views
import logging

app_name = 'fortunaisk'

# Hook pour ajouter l'entrée dans le menu principal
class RaffleMenu(MenuItemHook):
    def __init__(self):
        logger.debug("[DEBUG] Hook RaffleMenu chargé pour FortunaISK.")
        super().__init__(
            _('FortunaISK'),
            'fortunaisk:main_view',
            navactive=['fortunaisk']
        )

    def permissions(self, user):
        return user.has_perm('fortunaisk.view_raffle')  # Vérifiez les permissions

MenuItemHook.register(RaffleMenu)

urlpatterns = [
    path('', views.main_view, name='main_view'),
    path('history/', views.history_view, name='history_view'),
]
