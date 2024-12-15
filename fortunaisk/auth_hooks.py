from allianceauth import hooks
from allianceauth.services.hooks import UrlHook, MenuItemHook

class FortunaISKUrls(UrlHook):
    def __init__(self):
        from . import urls
        super().__init__((urls.urlpatterns, 'fortunaisk'), 'fortunaisk', 'fortunaisk/')

# Important: 
# Assurez-vous que le UrlHook est enregistré avant le MenuItemHook

@hooks.register('url_hook')
def register_urls():
    return FortunaISKUrls()

class FortunaISKMenu(MenuItemHook):
    def __init__(self):
        # Arguments positionnels: texte, url_name, icône, etc.
        super().__init__(
            'FortunaISK',               # Le texte affiché dans le menu
            'fortunaisk:current_lottery', # Le nom du pattern d'URL
            'fa fa-ticket',             # L'icône Font Awesome
            navactive=['fortunaisk:']
        )


@hooks.register('menu_item_hook')
def register_menu():
    return FortunaISKMenu()
