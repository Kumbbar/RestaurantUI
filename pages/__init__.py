from flet_core import Container, Page, transform

from services.requests.auth import AuthService


class BasePage(Container):
    def __init__(self, page: Page):
        super().__init__()
        self.padding = 0
        self.page = page
        self.expand = True
        self.offset = transform.Offset(0, 0, )
        page.current_view = self
        self.auth_service = AuthService(page)
