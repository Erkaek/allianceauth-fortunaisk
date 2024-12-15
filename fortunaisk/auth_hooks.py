from allianceauth import hooks
from allianceauth.services.hooks import UrlHook, MenuItemHook
from django.urls import reverse

class FortunaISKUrls(UrlHook):
    def __init__(self):
        from . import urls
        super().__init__((urls.urlpatterns, 'fortunaisk'), 'fortunaisk', 'fortunaisk/')

class FortunaISKMenu(MenuItemHook):
    def __init__(self):
        # Le deuxième argument doit être une URL déjà résolue,
        # par exemple via reverse(), et non le nom du pattern.
        super().__init__(
            'FortunaISK',
            reverse('fortunaisk:current_lottery'),  # URL résolue grâce à reverse
            'fa fa-ticket',                         # Icône en troisième argument
            navactive=['fortunaisk:']
        )

@hooks.register('url_hook')
def register_urls():
    return FortunaISKUrls()

@hooks.register('menu_item_hook')
def register_menu():
    return FortunaISKMenu()
