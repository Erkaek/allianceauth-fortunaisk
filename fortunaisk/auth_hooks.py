from allianceauth import hooks
from allianceauth.services.hooks import MenuItemHook, UrlHook
from .models import Ticket
from . import urls


class FortunaTicketsMenu(MenuItemHook):
    def __init__(self):
        super().__init__(
            "Fortuna Tickets",
            "fas fa-ticket-alt fa-fw",
            "fortunaisk:list",  # URL de base pour afficher les tickets
            navactive=["fortunaisk:"]
        )

    def render(self, request):
        # Vérifier si l'utilisateur a des tickets non payés
        if request.user.is_authenticated:
            unpaid_tickets = Ticket.objects.filter(
                character__character_ownership__user=request.user, paid=False
            ).count()
            if unpaid_tickets > 0:
                self.count = unpaid_tickets  # Ajoute un compteur pour les tickets non payés
        return super().render(request)


@hooks.register("menu_item_hook")
def register_menu():
    return FortunaTicketsMenu()


@hooks.register("url_hook")
def register_url():
    return UrlHook(urls, "fortunaisk", r"^fortunaisk/")


@hooks.register("discord_cogs_hook")
def register_cogs():
    return ["fortunaisk.cogs"]
