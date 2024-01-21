import flet as ft
from consts.colors import PastelColors
from consts.sizes import BUTTON_HEIGHT


class MainPage(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.offset = ft.transform.Offset(0, 0, )
        self.expand = True
        self.view_hide_text = ft.Text(
            value='View',
            color=PastelColors.WHITE_BASE,
            font_family='poppins medium',

        )
        self.content = ft.Container(
            alignment=ft.alignment.center,
            on_click=lambda _: page.go('/login'),
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
        self.page.go('/login')
