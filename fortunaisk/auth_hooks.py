# fortunaisk/auth_hooks.py

from allianceauth import hooks
from allianceauth.services.hooks import MenuItemHook, UrlHook
from django.urls import reverse
from . import urls

@hooks.register('url_hook')
def register_url():
    # Enregistre les URLs de l'application sous le namespace 'fortunaisk' et le préfixe 'fortunaisk/'
    return UrlHook(urls.urlpatterns, 'fortunaisk', 'fortunaisk/')

class FortunaISKMenu(MenuItemHook):
    def __init__(self):
        # Initialise le MenuItemHook avec le texte, l'icône et le nom de l'URL
        super().__init__(
            'FortunaISK',                     # Texte affiché dans le menu
            'fa fa-ticket',                   # Icône Font Awesome
            'fortunaisk:current_lottery',     # Nom du pattern d'URL
            navactive=['fortunaisk:']         # Namespace pour activer l'élément de menu
        )

@hooks.register('menu_item_hook')
def register_menu():
    return FortunaISKMenu()
