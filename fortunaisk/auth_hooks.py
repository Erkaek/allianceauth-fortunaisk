from allianceauth import hooks
from allianceauth.services.hooks import UrlHook, MenuItemHook

class FortunaISKUrls(UrlHook):
    def __init__(self):
        from . import urls
        # On passe un tuple (urlpatterns, app_name) et on ajoute namespace et base_url
        super().__init__((urls.urlpatterns, 'fortunaisk'), 'fortunaisk', 'fortunaisk/')

class FortunaISKMenu(MenuItemHook):
    def __init__(self):
        # Arguments : text, url_name, icon, navactive
        # On donne un nom de pattern d'URL, pas une URL résolue par reverse()
        super().__init__(
            text='FortunaISK',
            url_name='fortunaisk:current_lottery',
            icon='fa fa-ticket',
            navactive=['fortunaisk:']
        )

@hooks.register('url_hook')
def register_urls():
    return FortunaISKUrls()

@hooks.register('menu_item_hook')
def register_menu():
    return FortunaISKMenu()
