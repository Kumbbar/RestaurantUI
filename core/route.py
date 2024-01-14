from flet_core import UserControl, Page

from core.urls import view_urls
from pages.views import StyleView


class BasePageRouteHandler(UserControl):
    def __init__(self, page: Page):
        super().__init__()
        self.page = page
        self.page.on_route_change = self.on_route_change

    def on_route_change(self, route):
        new_page = view_urls[self.page.route](self.page)
        self.page.views.append(
            StyleView(route, [new_page])
        )
        self.page.update()

    def view_pop(self, view):
        self.page.views.pop()
        top_view = self.page.views[-1]
        self.page.go(top_view.route)


