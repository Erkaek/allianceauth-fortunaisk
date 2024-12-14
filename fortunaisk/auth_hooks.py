# fortunaisk/auth_hooks.py
from django.utils.translation import gettext_lazy as _
from allianceauth.services.hooks import get_extension_logger

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
    # Ici vous pourriez ajouter de la logique d'initialisation,
    # comme des signaux, du code de setup, etc.
