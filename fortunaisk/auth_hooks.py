from django.urls import reverse
from allianceauth import hooks

@hooks.register('services_hook')
def fortunaisk_service():
    return {
        'app_name': 'fortunaisk',
        'name': 'FortunaISK',
        'icon': 'fa fa-ticket',
        'urls': 'fortunaisk.urls',  # indique à AllianceAuth où trouver vos urls
    }

@hooks.register('menu_item_hook')
def fortunaisk_menu():
    return {
        'name': 'FortunaISK',
        'icon': 'fa fa-ticket',
        'children': [
            {'name': 'Loterie en cours', 'url': reverse('fortunaisk:current_lottery')},
            {'name': 'Historique des gagnants', 'url': reverse('fortunaisk:winners_history')}
        ]
    }