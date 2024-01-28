from flet_core import Page, RouteChangeEvent

from services.auth import AuthService
from settings import LOGIN_PAGE_VIEW_URL, MAIN_PAGE_VIEW_URL
from .urls import view_urls
from .views import StyleView


class BasePageRouteHandler(object):
    def __init__(self, page: Page):
        super().__init__()
        self.page = page
        self.page.on_route_change = self.on_route_change

    def on_route_change(self, route: RouteChangeEvent):
        auth_service = AuthService(self.page)
        if route.route != LOGIN_PAGE_VIEW_URL and not auth_service.is_authenticated:
            self.page.go(LOGIN_PAGE_VIEW_URL)
            return
        try:
            new_page = view_urls[self.page.route](self.page)
        except KeyError:
            self.page.go(MAIN_PAGE_VIEW_URL)
            return
        self.page.views.append(
            StyleView(route, [new_page])
        )
        self.page.update()

    def view_pop(self, view):
        self.page.views.pop()
        top_view = self.page.views[-1]
        self.page.go(top_view.route)


