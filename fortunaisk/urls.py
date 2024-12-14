from django.urls import path
from allianceauth.services.hooks import MenuItemHook
from django.utils.translation import gettext_lazy as _
from . import views

app_name = 'fortunaisk'

# Hook pour le menu
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

urlpatterns = [
    path('', views.main_view, name='main_view'),
    path('history/', views.history_view, name='history_view'),
]
