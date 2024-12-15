from allianceauth import hooks
from allianceauth.services.hooks import MenuItemHook, UrlHook
from . import urls

class FortunaMenu(MenuItemHook):
    def __init__(self):
        super().__init__(
            "Fortuna Tickets",
            "fas fa-ticket-alt fa-fw",  # Icône de menu
            "fortunaisk:tickets_list",  # Nom d'URL correspondant à la liste des tickets
            navactive=["fortunaisk:"]
        )

@hooks.register("menu_item_hook")
def register_menu():
    return FortunaMenu()

@hooks.register("url_hook")
def register_url():
    return UrlHook(urls, "fortunaisk", r"^fortunaisk/")
