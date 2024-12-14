from allianceauth.services.hooks import MenuItemHook, UrlHook
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

# Enregistrez le menu
MenuItemHook.register(FortunaISKMenu)

# Enregistrez les URL
@hooks.register("url_hook")
def register_urls():
    return UrlHook(urls, "fortunaisk", r"^fortunaisk/")
