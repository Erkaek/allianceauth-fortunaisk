from allianceauth.services.hooks import MenuItemHook, UrlHook
from django.urls import reverse

class FortunaISKMenuItem(MenuItemHook):
    def __init__(self):
        super().__init__(
            name="FortunaISK",
            url=reverse('fortunaisk:index'),
            icon="fas fa-dice",
            perm="fortunaisk.view_fortunaisk",
        )

class FortunaISKUrls(UrlHook):
    def __init__(self):
        super().__init__(
            urls='fortunaisk.urls',
            namespace='fortunaisk',
        )

# Enregistrer les hooks
menu_item_hook = FortunaISKMenuItem()
url_hook = FortunaISKUrls()
