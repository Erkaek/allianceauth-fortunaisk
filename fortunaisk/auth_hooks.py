from allianceauth.services.hooks import MenuItemHook, UrlHook
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

class FortunaISKMenuItem(MenuItemHook):
    def __init__(self):
        super().__init__(
            _('FortunaISK'),
            'fas fa-dice',
            'fortunaisk:index',
            navactive=['fortunaisk:'],
            order=1001
        )

    def render(self, request):
        if request.user.has_perm('fortunaisk.view_fortunaisk'):
            return super().render(request)
        return ''

@hooks.register('menu_item_hook')
def register_menu():
    return FortunaISKMenuItem()

@hooks.register('url_hook')
def register_urls():
    return UrlHook(urls, 'fortunaisk', r'^fortunaisk/')
