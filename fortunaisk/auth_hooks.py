"""Hook into Alliance Auth"""

# Django
from django.utils.translation import gettext_lazy as _

# Alliance Auth
from allianceauth import hooks
from allianceauth.services.hooks import MenuItemHook, UrlHook

# FortunaISK
from fortunaisk import urls


class FortunaISKMenuItem(MenuItemHook):
    """Menu item for FortunaISK"""

    def __init__(self):
        # Set up menu entry for sidebar
        super().__init__(
            _("FortunaISK"),  # Display name
            "fas fa-ticket-alt fa-fw",  # Font Awesome icon
            "fortunaisk:main_view",  # URL name
            navactive=["fortunaisk:"],  # Highlight menu when active
        )

    def render(self, request):
        """Render the menu item"""

        # Check if the user has the necessary permissions
        if request.user.has_perm("fortunaisk.view_raffle"):
            return super().render(request)
        return ""  # Return empty if the user lacks permissions


@hooks.register("menu_item_hook")
def register_menu():
    """Register the menu item for FortunaISK"""
    return FortunaISKMenuItem()


@hooks.register("url_hook")
def register_urls():
    """Register app URLs"""
    return UrlHook(urls, "fortunaisk", r"^fortunaisk/")
