# fortunaisk/auth_hooks.py
from allianceauth import hooks
from allianceauth.services.hooks import UrlHook, MenuItemHook
from django.urls import reverse

class FortunaISKUrls(UrlHook):
    def __init__(self):
        from . import urls
        # On passe un tuple (urlpatterns, 'app_name')
        super().__init__((urls.urlpatterns, 'fortunaisk'), 'fortunaisk', 'fortunaisk/')

class FortunaISKMenu(MenuItemHook):
    def __init__(self):
        # text = 'FortunaISK'
        # url_name = 'fortunaisk:current_lottery' (le nom du pattern d'url)
        # icon = 'fa fa-ticket'
        # navactive = ['fortunaisk:']
        super().__init__(
            'FortunaISK',
            'fortunaisk:current_lottery',
            'fa fa-ticket',
            navactive=['fortunaisk:']
        )

@hooks.register('url_hook')
def register_urls():
    return FortunaISKUrls()

@hooks.register('menu_item_hook')
def register_menu():
    return FortunaISKMenu()
