import flet as ft
from consts.colors import PastelColors
from consts.sizes import BUTTON_HEIGHT
from pages.base import BasePage
from settings import LOGIN_PAGE_VIEW_URL, SESSION_TOKEN_KEY


class MainPage(BasePage):
    def __init__(self, page: ft.Page):
        super().__init__(page)
        print(id(page), 'main page')

        self.offset = ft.transform.Offset(0, 0, )
        print(page.client_storage.get_keys('token'), 'init')
        self.expand = True
        self.view_hide_text = ft.Text(
            value='View',
            color=PastelColors.WHITE_BASE,
            font_family='poppins medium',

        )
        self.content = ft.Container(
            alignment=ft.alignment.center,
            on_click=self.back_click,
            height=50, width=150,
            bgcolor='white',
            content=ft.Text(
                value='Get Started',
                size=20,
                color='black'
            )
        )
        self.button = ft.Container(
            height=BUTTON_HEIGHT,
            width=BUTTON_HEIGHT,
            on_click=self.back_click,
            bgcolor=PastelColors.DARK_BROWN,
            border_radius=10,
            alignment=ft.alignment.center,
            content=ft.Text(
                value='Continue',
                font_family='Poppins Medium',
                size=16,

            )
        )

    def back_click(self, e):
        self.auth_service.logout_user()
        if not self.auth_service.is_authenticated:
            self.page.go(LOGIN_PAGE_VIEW_URL)

