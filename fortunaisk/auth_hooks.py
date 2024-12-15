from allianceauth import hooks
from allianceauth.services.hooks import UrlHook
from django.urls import reverse

@hooks.register('url_hook')
def fortunaisk_url_hook():
    # Import des URL patterns de l'app
    from fortunaisk import urls
    # On retourne une instance de UrlHook
    # urls.urlpatterns : la liste de vos urls
    # 'fortunaisk' : le namespace
    # 'fortunaisk/' : le préfixe d'URL
    return UrlHook(urls.urlpatterns, 'fortunaisk', base_url='fortunaisk/')

@hooks.register('menu_item_hook')
def fortunaisk_menu():
    # Maintenant, le namespace 'fortunaisk' est enregistré via le url_hook
    return {
        'name': 'FortunaISK',
        'icon': 'fa fa-ticket',
        'children': [
            {'name': 'Loterie en cours', 'url': reverse('fortunaisk:current_lottery')},
            {'name': 'Historique des gagnants', 'url': reverse('fortunaisk:winners_history')}
        ]
    }
