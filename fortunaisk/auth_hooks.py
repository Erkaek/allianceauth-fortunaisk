from allianceauth import hooks
from allianceauth.services.hooks import MenuItemHook, UrlHook

from . import urls


class FortunaiskMenuItem(MenuItemHook):
    """Menu entry for Fortunaisk, visible only to authorized users"""

    def __init__(self):
        # Initialize menu entry for Fortunaisk in the sidebar
        MenuItemHook.__init__(
            self,
            "Fortunaisk",
            "fas fa-coins fa-fw",
            "fortunaisk:tickets_list",  # Correction ici pour correspondre à l'URL dans urls.py
            navactive=["fortunaisk:"],
        )

    def render(self, request):
        # Only render the menu for users with appropriate permissions
        if request.user.has_perm("fortunaisk.view_ticket"):
            return MenuItemHook.render(self, request)
        return ""


@hooks.register("menu_item_hook")
def register_menu():
    return FortunaiskMenuItem()


@hooks.register("url_hook")
def register_urls():
    # Register URL patterns for Fortunaisk
    return UrlHook(urls, "fortunaisk", r"^fortunaisk/")
