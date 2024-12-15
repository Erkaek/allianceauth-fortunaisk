from allianceauth import hooks
from allianceauth.services.hooks import UrlHook, MenuItemHook
from django.urls import reverse
from . import urls

class FortunaISKUrlHook(UrlHook):
    def __init__(self):
        # Même logique que l’invoice_manager : super().__init__(urlpatterns, app_name, base_url)
        super().__init__(urls.urlpatterns, 'fortunaisk', 'fortunaisk/')

class FortunaISKMenuItem(MenuItemHook):
    def __init__(self):
        # On suit l’exemple de l’invoice_manager :
        # Arguments : text, url (résolue avec reverse), icon, navactive
        super().__init__(
            'FortunaISK',
            reverse('fortunaisk:current_lottery'), # URL résolue
            'fa fa-ticket',                        # Icône Font Awesome
            navactive=['fortunaisk:']
        )

@hooks.register('url_hook')
def register_urls():
    return FortunaISKUrlHook()

@hooks.register('menu_item_hook')
def register_menu():
    return FortunaISKMenuItem()
