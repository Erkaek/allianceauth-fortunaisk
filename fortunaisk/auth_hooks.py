from allianceauth import hooks
from allianceauth.services.hooks import MenuItemHook, UrlHook

from fortunaisk import models

from . import app_settings, urls
from .models import FortunaISKModel


class FortunaISKMenu(MenuItemHook):
    def __init__(self):
        # Utilise les mêmes paramètres que le module `invoice`
        super().__init__(
            app_settings.APP_NAME,  # Nom affiché dans le menu
            'fas fa-coins fa-fw',  # Icône
            'fortunaisk:index',  # URL par défaut
            navactive=['fortunaisk:']
        )

    def render(self, request):
        if request.user.has_perm('fortunaisk.access_fortunaisk'):
            # Exemple : afficher un compteur pour un modèle spécifique
            item_count = FortunaISKModel.objects.filter(
                user=request.user, is_active=True
            ).count()
            if item_count:
                self.count = item_count
            return super().render(request)
        return ''


@hooks.register('menu_item_hook')
def register_menu():
    """Enregistre l'entrée dans le menu principal"""
    return FortunaISKMenu()


@hooks.register('url_hook')
def register_url():
    """Déclare les URLs du module"""
    return UrlHook(
        urls='fortunaisk.urls',  # Fichier urls.py dans le module
        namespace='fortunaisk',  # Namespace du module
        base_url=r'^fortunaisk/'  # Base URL pour les routes
    )


@hooks.register("secure_group_filters")
def filters():
    """Déclare les filtres de groupes sécurisés (si nécessaire)"""
    return [models.NoOverdueFilter, models.TotalISKFilter]


@hooks.register('discord_cogs_hook')
def register_cogs():
    """Enregistre les cogs pour Discord"""
    return ["fortunaisk.cogs"]
