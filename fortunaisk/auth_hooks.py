from allianceauth.hooks import DashboardHook

class FortunaISKDashboard(DashboardHook):
    """
    Widget pour le tableau de bord d'Alliance Auth.
    """
    def render(self, request):
        # Assurez-vous que seuls les utilisateurs autorisés voient ce widget
        if request.user.has_perm("fortunaisk.view_raffle"):
            return """
            <div class="panel panel-default">
                <div class="panel-heading">FortunaISK Lottery</div>
                <div class="panel-body">
                    <p>Participate in this month's lottery and win big!</p>
                    <a href="/fortunaisk/" class="btn btn-primary">Go to FortunaISK</a>
                </div>
            </div>
            """
        return ""

# Enregistrez le hook
DashboardHook.register(FortunaISKDashboard)
