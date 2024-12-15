from allianceauth.services.hooks import UrlHook, MenuItemHook
from allianceauth.services.hooks.models import MenuItem
from django.urls import reverse

class FortunaISKUrls(UrlHook):
    def __init__(self):
        super().__init__([("fortunaisk.urls", "fortunaisk")], 'fortunaisk', 'fortunaisk/')

class FortunaISKMenu(MenuItemHook):
    def __init__(self):
        super().__init__([
            MenuItem(
                name="FortunaISK",
                url=reverse('fortunaisk:index'),
                perm="fortunaisk.access_fortunaisk",
                icon="fas fa-dice"
            )
        ])

url_hook = FortunaISKUrls()
menu_hook = FortunaISKMenu()
