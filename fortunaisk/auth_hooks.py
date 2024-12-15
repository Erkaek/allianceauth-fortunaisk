from allianceauth import hooks
from allianceauth.services.hooks import MenuItemHook, UrlHook
from .models import Ticket  # Utilisation de Ticket à la place de FortunaISKModel
from . import urls

class FortunaMenu(MenuItemHook):
    def __init__(self):
        MenuItemHook.__init__(
            self,
            "Fortuna Tickets",
            "fas fa-ticket-alt fa-fw",
            "fortunaisk:list",  # Vue associée
            navactive=["fortunaisk:"]
        )

    def render(self, request):
        # Exemple pour afficher un compteur basé sur les tickets non payés
        unpaid_tickets = Ticket.objects.filter(paid=False).count()
        if unpaid_tickets > 0:
            self.count = unpaid_tickets
        return super().render(request)

@hooks.register("menu_item_hook")
def register_menu():
    return FortunaMenu()

@hooks.register("url_hook")
def register_url():
    return UrlHook(urls, "fortunaisk", r"^fortunaisk/")
