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
        # text = 'FortunaISK'
        # url_name = 'fortunaisk:current_lottery'
        # icon = 'fas fa-ticket' (solide, cohérent avec FA5+)
        super().__init__(
            'FortunaISK',
            'fortunaisk:current_lottery',
            'fas fa-ticket',
            navactive=['fortunaisk:']
        )

@hooks.register('menu_item_hook')
def register_menu():
    return FortunaISKMenu()
