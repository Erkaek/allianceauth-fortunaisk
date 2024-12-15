# fortunaisk/auth_hooks.py

from allianceauth import hooks
from allianceauth.services.hooks import MenuItemHook, UrlHook
from django.urls import reverse
from . import urls

class FortunaISKUrls(UrlHook):
    def __init__(self):
        # Assurez-vous que 'urls.urlpatterns' est passé comme premier argument
        super().__init__(urls.urlpatterns, 'fortunaisk', 'fortunaisk/')

class FortunaISKMenu(MenuItemHook):
    def __init__(self):
        super().__init__(
            'FortunaISK',                    # Texte affiché dans le menu
            'fa fa-ticket',                  # Icône Font Awesome
            'fortunaisk:current_lottery',    # Nom du pattern d'URL
            navactive=['fortunaisk:']        # Namespace pour activer l'élément de menu
        )

@hooks.register('url_hook')
def register_urlhook():
    return FortunaISKUrls()

@hooks.register('menu_item_hook')
def register_menuhook():
    return FortunaISKMenu()
