from allianceauth import hooks
from allianceauth.services.hooks import UrlHook, MenuItemHook
from django.urls import reverse

class FortunaISKUrls(UrlHook):
    def __init__(self):
        from . import urls
        super().__init__((urls.urlpatterns, 'fortunaisk'), 'fortunaisk', 'fortunaisk/')

class FortunaISKMenu(MenuItemHook):
    def __init__(self):
        super().__init__(
            'FortunaISK',                  # Texte de l'item
            'fortunaisk:current_lottery',  # Nom du pattern d'URL (DOIT ÊTRE LE 2e argument)
            'fa fa-ticket',                # Icône (3e argument)
            navactive=['fortunaisk:']
        )


@hooks.register('url_hook')
def register_urls():
    return FortunaISKUrls()

@hooks.register('menu_item_hook')
def register_menu():
    return FortunaISKMenu()
