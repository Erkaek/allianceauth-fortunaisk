from allianceauth.services.hooks import MenuItemHook, UrlHook
from allianceauth.hooks import DashboardItemHook
from allianceauth import hooks
from django.utils.translation import gettext_lazy as _
from . import urls


class FortunaISKMenu(MenuItemHook):
    def __init__(self):
        super().__init__(
            _("FortunaISK"),
            "fas fa-ticket-alt",
            "fortunaisk:main_view",
            navactive=["fortunaisk:"]
        )

    def render(self, request):
        if request.user.has_perm("fortunaisk.view_raffle"):
            return super().render(request)
        return ""


class FortunaISKDashboardWidget(DashboardItemHook):
    """Widget pour le tableau de bord."""

    def __init__(self):
        super().__init__(_("FortunaISK Lottery"), "fortunaisk:main_view")

    def render(self, request):
        if request.user.has_perm("fortunaisk.view_raffle"):
            return """
            <div class="panel panel-default">
                <div class="panel-heading">FortunaISK</div>
                <div class="panel-body">
                    <p>Participate in this month's lottery and win big!</p>
                    <a href="/fortunaisk/" class="btn btn-primary">Go to FortunaISK</a>
                </div>
            </div>
            """
        return ""


@hooks.register("menu_item_hook")
def register_menu():
    return FortunaISKMenu()


@hooks.register("url_hook")
def register_urls():
    return UrlHook(urls, "fortunaisk", r"^fortunaisk/")


@hooks.register("dashboard_hook")
def register_dashboard():
    return FortunaISKDashboardWidget()
