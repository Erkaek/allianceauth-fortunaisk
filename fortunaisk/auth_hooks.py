from allianceauth import hooks
from django.urls import include, path, reverse

@hooks.register('url_hook')
def fortunaisk_url_hook():
    # Import des urls de l'app
    from fortunaisk import urls
    # On retourne un pattern qui inclut les URLs de l'app sous le namespace 'fortunaisk'
    return path('fortunaisk/', include((urls, 'fortunaisk'), namespace='fortunaisk'))


@hooks.register('menu_item_hook')
def fortunaisk_menu():
    # Maintenant que les URLs sont enregistrées via url_hook, 
    # le namespace 'fortunaisk' est connu de Django.
    return {
        'name': 'FortunaISK',
        'icon': 'fa fa-ticket',
        'children': [
            {'name': 'Loterie en cours', 'url': reverse('fortunaisk:current_lottery')},
            {'name': 'Historique des gagnants', 'url': reverse('fortunaisk:winners_history')}
        ]
    }
