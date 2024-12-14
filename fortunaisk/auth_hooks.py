# fortunaisk/auth_hooks.py
from django.utils.translation import gettext_lazy as _
from allianceauth.services.hooks import get_extension_logger, add_menu_item, MenuItemHook
from django.urls import reverse

logger = get_extension_logger(__name__)

__version__ = '0.1.0'
__title__ = 'FortunaISK'

def provides_app_settings():
    return {
        'name': __title__,
        'version': __version__,
        'description': _('A plugin to view and manage ISK fortunes within AllianceAuth'),
        'author': 'Votre Nom',
    }

def load():
    logger.info('Loading the FortunaISK plugin...')
    # Ajout d'un lien dans le menu du dashboard
    # Utilisez `reverse` pour pointer vers la vue `index` de votre plugin
    add_menu_item(
        MenuItemHook(
            name=_('FortunaISK'),
            url=reverse('fortunaisk:index'),  # Vérifiez que le namespace 'fortunaisk' est correct
            icon='fas fa-coins',  # Une icône FontAwesome de votre choix
            order=100  # Position dans le menu, plus petit = plus haut
        )
    )
