from allianceauth import hooks
from allianceauth.services.hooks import ServiceHook
from django.urls import include, path, reverse

class FortunaISKService(ServiceHook):
    name = 'FortunaISK'
    app_name = 'fortunaisk'
    icon = 'fa fa-ticket'

    @property
    def urlpatterns(self):
        # Import local URLs ici pour éviter les références circulaires
        from fortunaisk import urls
        # On inclut les URLs de l'app avec le namespace fortunaisk
        return [
            path('', include((urls, self.app_name), namespace=self.app_name)),
        ]

@hooks.register('services_hook')
def fortunaisk_service():
    # On retourne la classe, pas une instance
    return FortunaISKService

@hooks.register('menu_item_hook')
def fortunaisk_menu():
    # Maintenant que le service est enregistré, le namespace 'fortunaisk' est connu
    return {
        'name': 'FortunaISK',
        'icon': 'fa fa-ticket',
        'children': [
            {'name': 'Loterie en cours', 'url': reverse('fortunaisk:current_lottery')},
            {'name': 'Historique des gagnants', 'url': reverse('fortunaisk:winners_history')}
        ]
    }
