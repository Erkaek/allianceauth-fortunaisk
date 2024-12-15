# fortunaisk/auth_hooks.py

from allianceauth import hooks
from allianceauth.services.hooks import MenuItemHook, UrlHook
from . import urls

# D'abord, on enregistre les URLs via un UrlHook en suivant le même principe que corptools
@hooks.register('url_hook')
def register_url():
    # Ici, on inclut les urls du module fortunaisk sous le namespace 'fortunaisk'
    # et on leur donne un préfixe d'URL. Par exemple '^fortunaisk/' pour préfixer les urls.
    return UrlHook(urls, 'fortunaisk', r'^fortunaisk/')

# Ensuite, on crée la classe pour le menu
class FortunaISKMenu(MenuItemHook):
    def __init__(self):
        # Selon l'exemple corptools :
        # MemberAudit: MenuItemHook.__init__(self, app_settings.CORPTOOLS_APP_NAME, 'far fa-eye fa-fw', 'corptools:react', ...)
        # On suit donc le même pattern : (text, icon, url_name, ...)
        #
        # text = "FortunaISK"
        # icon = "fa fa-ticket"
        # url_name = "fortunaisk:current_lottery"
        #
        # navactive = ['fortunaisk:'] permet de marquer l'item actif sur les pages fortunaisk
        MenuItemHook.__init__(
            self,
            'FortunaISK',                 # texte affiché
            'fa fa-ticket',               # icône Font Awesome
            'fortunaisk:current_lottery', # nom du pattern d'URL
            navactive=['fortunaisk:']
        )

@hooks.register('menu_item_hook')
def register_menu():
    return FortunaISKMenu()
