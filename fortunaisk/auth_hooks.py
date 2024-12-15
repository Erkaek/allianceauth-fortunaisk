from allianceauth import hooks
from allianceauth.services.hooks import MenuItemHook
from django.urls import reverse

class FortunaISKMenu(MenuItemHook):
    def __init__(self):
        # Arguments: text, url_name_or_url, icon, navactive
        super().__init__(
            'FortunaISK',
            reverse('fortunaisk:current_lottery'),
            'fa fa-ticket',
            navactive=['fortunaisk:']
        )
        # Pour avoir un sous-menu, ajoutez des enfants :
        self.children = [
            MenuItemHook(
                'Current Lottery',
                'fortunaisk:current_lottery',
                'fa fa-ticket',
                navactive=['fortunaisk:current_lottery']
            ),
            MenuItemHook(
                'Winners History',
                'fortunaisk:winners_history',
                'fa fa-trophy',
                navactive=['fortunaisk:winners_history']
            )
        ]

@hooks.register('menu_item_hook')
def register_menu():
    return FortunaISKMenu()
