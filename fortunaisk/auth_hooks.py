# fortunaisk/auth_hooks.py
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from allianceauth.hooks import register_hook

__version__ = '0.1.0'
__title__ = 'FortunaISK'

def provides_app_settings():
    return {
        'name': __title__,
        'version': __version__,
        'description': _('A plugin to view and manage ISK fortunes'),
        'author': 'Votre Nom',
    }

def load():
    # Aucun import de MenuItemHook ou UrlHook ici
    # Pas de code d'enregistrement direct du menu ou des URLs ici
    pass

@register_hook('url_hook')
def fortunaisk_urls():
    # On indique à AllianceAuth quel module d’URLs utiliser, ainsi que le namespace et l’app_name
    return ('fortunaisk.urls', 'fortunaisk', 'fortunaisk')

@register_hook('menu_item_hook')
def fortunaisk_menu_item():
    # On ajoute un item de menu pour le dashboard
    return {
        'name': _('FortunaISK'),
        'icon': 'fas fa-coins',  # Une icône FontAwesome
        'url': reverse('fortunaisk:index'),
        'groups': {'all': True},  # Visible par tous les utilisateurs authentifiés
    }
