from allianceauth import hooks
from allianceauth.services.hooks import UrlHook
from django.urls import reverse

class FortunaISKUrlHook(UrlHook):
    app_name = 'fortunaisk'
    url_module = 'fortunaisk.urls'

    def __init__(self):
        super().__init__()

@hooks.register('url_hook')
def fortunaisk_url_hook():
    # Retourne une instance du hook URL
    return FortunaISKUrlHook()

@hooks.register('menu_item_hook')
def fortunaisk_menu():
    # Maintenant que les URLs sont gérées par le UrlHook,
    # le namespace 'fortunaisk' est connu et on peut faire reverse()
    return {
        'name': 'FortunaISK',
        'icon': 'fa fa-ticket',
        'children': [
            {'name': 'Loterie en cours', 'url': reverse('fortunaisk:current_lottery')},
            {'name': 'Historique des gagnants', 'url': reverse('fortunaisk:winners_history')}
        ]
    }
