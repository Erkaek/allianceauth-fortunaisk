from allianceauth.services.hooks import MenuItemHook, UrlHook
from allianceauth import hooks
from django.utils.translation import gettext_lazy as _
from . import urls


class FortunaISKMenu(MenuItemHook):
    """
    Menu entry for FortunaISK.
    """
    def __init__(self):
        super().__init__(
            _("FortunaISK"),
            "fas fa-ticket-alt",  # Icône Font Awesome
            "fortunaisk:main_view",
            navactive=["fortunaisk:"]
        )

    def render(self, request):
        # Vérifiez les permissions avant d'afficher l'entrée du menu
        if request.user.has_perm("fortunaisk.view_raffle"):
            return super().render(request)
        return ""


@hooks.register("menu_item_hook")
def register_menu():
    """
    Enregistre le menu pour le module FortunaISK.
    """
    return FortunaISKMenu()


@hooks.register("url_hook")
def register_urls():
    """
    Enregistre les URL pour le module FortunaISK.
    """
    return UrlHook(urls, "fortunaisk", r"^fortunaisk/")
