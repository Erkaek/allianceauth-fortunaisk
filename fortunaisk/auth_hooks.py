# fortunaisk/auth_hooks.py
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from allianceauth.hooks import MenuItemHook, UrlHook
from . import urls

def provides_app_settings():
    return {
        'name': 'FortunaISK',
        'version': '0.1.0',
        'description': _('A plugin to view and manage ISK fortunes'),
        'author': 'Votre Nom',
    }

def load():
    # Aucune insertion de menu direct ici, c'est géré par les décorateurs
    pass

@UrlHook()
def register_urls():
    return urls, 'fortunaisk', 'fortunaisk'

@MenuItemHook()
def register_menu():
    return {
        'name': _('FortunaISK'),
        'icon': 'fas fa-coins',
        'url': reverse('fortunaisk:index'),
        'groups': {'all': True},
    }
