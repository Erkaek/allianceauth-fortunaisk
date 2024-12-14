from django.urls import path
from allianceauth.services.hooks import MenuItemHook
from django.utils.translation import gettext_lazy as _
from . import views

app_name = 'fortunaisk'

# Hook pour ajouter "FortunaISK" au menu principal
class RaffleMenu(MenuItemHook):
    def __init__(self):
        super().__init__(
            _('FortunaISK'),
            'fortunaisk:main_view',
            navactive=['fortunaisk']
        )

    def permissions(self, user):
        return user.has_perm('fortunaisk.view_raffle')

MenuItemHook.register(RaffleMenu)

# Routes internes du module
urlpatterns = [
    path('', views.main_view, name='main_view'),  # Vue principale
    path('history/', views.history_view, name='history_view'),  # Vue historique des gagnants
]
