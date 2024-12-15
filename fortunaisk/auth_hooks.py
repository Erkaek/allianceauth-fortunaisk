from allianceauth.services.hooks import hooks, MenuItemHook, UrlHook
from allianceauth.services.hooks.models import MenuItem
from django.urls import reverse

class FortunaISKMenuItem(MenuItemHook):
    def __init__(self):
        super().__init__(
            name="FortunaISK",
            url=reverse('fortunaisk:index'),
            icon="fas fa-dice",
            perm="fortunaisk.view_fortunaisk",
        )

@hooks.register('menu_item_hook')
def register_menu_hook():
    return FortunaISKMenuItem()

@hooks.register('url_hook')
def register_url_hook():
    return UrlHook(urls='fortunaisk.urls', namespace='fortunaisk')
