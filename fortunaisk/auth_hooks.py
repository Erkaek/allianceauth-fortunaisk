from allianceauth import hooks
from django.urls import reverse

class FortunaISKMenuItem(hooks.NavigationExtension):
    def nav_items(self, request, context):
        if request.user.is_authenticated:
            return [
                {
                    'title': 'FortunaISK',
                    'url': reverse('fortunaisk:current_lottery'),
                    'icon': 'fa fa-ticket',
                    'children': [
                        {'title': 'Loterie en cours', 'url': reverse('fortunaisk:current_lottery')},
                        {'title': 'Historique des gagnants', 'url': reverse('fortunaisk:winners_history')}
                    ]
                }
            ]
        return []

hooks.register('navigation_extension', FortunaISKMenuItem)
