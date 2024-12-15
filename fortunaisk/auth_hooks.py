from allianceauth import hooks
from allianceauth.services.hooks import MenuItemHook, UrlHook


class FortunaiskMenu(MenuItemHook):
    def __init__(self):
        super().__init__(
            name="Fortunaisk",
            icon_class="fas fa-coins fa-fw",
            url_name="fortunaisk:ticket_list",
            navactive=["fortunaisk:"]
        )

    def render(self, request):
        if request.user.has_perm('fortunaisk.view_ticket'):
            return super().render(request)
        return ''


@hooks.register('menu_item_hook')
def register_menu():
    return FortunaiskMenu()


@hooks.register('url_hook')
def register_urls():
    from . import urls
    return UrlHook(urls, 'fortunaisk', r'^fortunaisk/')
