from allianceauth import hooks
from allianceauth.services.hooks import UrlHook, MenuItemHook

class FortunaISKUrls(UrlHook):
    def __init__(self):
        from . import urls
        # On passe (urlpatterns, app_name), puis namespace, puis base_url
        super().__init__((urls.urlpatterns, 'fortunaisk'), 'fortunaisk', 'fortunaisk/')

class FortunaISKMenu(MenuItemHook):
    def __init__(self):
        # On passe les arguments positionnellement :
        # 1er: text
        # 2ème: url_name
        # 3ème: icon (optionnel)
        # navactive en argument nommé est permis
        super().__init__(
            'FortunaISK',               # text
            'fortunaisk:current_lottery',  # url_name (nom du pattern d'URL, pas reverse())
            'fa fa-ticket',             # icon en 3ème argument, sans nom
            navactive=['fortunaisk:']   # argument nommé autorisé
        )

@hooks.register('url_hook')
def register_urls():
    return FortunaISKUrls()

@hooks.register('menu_item_hook')
def register_menu():
    return FortunaISKMenu()
