from allianceauth import hooks
from django.urls import reverse

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
