# fortunaisk/auth_hooks.py
from django.utils.translation import gettext_lazy as _
from allianceauth.hooks import MenuItemHook, UrlHook
from django.urls import include, path, reverse

@UrlHook()
def fortunaisk_urls():
    # Inclut les URLs de l’app fortunaisk
    return path('fortunaisk/', include('fortunaisk.urls', namespace='fortunaisk'))

@MenuItemHook()
def fortunaisk_menu_item(request):
    return {
        'name': _('FortunaISK'),
        'url': reverse('fortunaisk:index'),
        'icon': 'fas fa-coins',
        'order': 100,
        'groups': {'all': True}  # accessible à tous les utilisateurs connectés
    }
