# auth_hooks.py
from allianceauth.services.hooks import MenuItemHook, UrlHook
from django.urls import reverse_lazy

class FortunaISKMenu(MenuItemHook):
    def __init__(self):
        super().__init__(
            name="FortunaISK",
            url=reverse_lazy('fortunaisk:index'),
            icon="fas fa-dice",
            perm="fortunaisk.view_tickets"
        )

@hooks.register('menu_item_hook')
def register_menu():
    return FortunaISKMenu()

@hooks.register('url_hook')
def register_url():
    return UrlHook(urls='fortunaisk.urls', namespace='fortunaisk')
