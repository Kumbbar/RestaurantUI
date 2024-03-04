import flet_core as ft

from consts.colors import PastelColors
from settings import LOGIN_PAGE_VIEW_URL


class BottomSheetServiceUnavailable(ft.BottomSheet):
    def __init__(self):
        super().__init__()
        self.content = ft.Container(
            padding=ft.Padding(20, 10, 20, 10),
            width=500,
            content=ft.Column(
                [
                    ft.Text("Server unavailable", size=18, weight=ft.FontWeight.BOLD),
                    ft.Text("Contact to developers if you need", size=14),
                ],
                tight=True,
            ),
        )
        self.bgcolor = PastelColors.BROWN_RED
        self.open = True


class BottomSheetInvalidToken(ft.BottomSheet):
    def __init__(self):
        super().__init__()
        self.content = ft.Container(
            padding=ft.Padding(20, 10, 20, 10),
            width=500,
            content=ft.Column(
                [
                    ft.Text("Your token expired. Log in again.", size=18, weight=ft.FontWeight.BOLD),
                    ft.Text("Contact to developers if you need", size=14),
                    ft.ElevatedButton(
                        'Log in',
                        bgcolor=PastelColors.LIGHT_BROWN,
                        color=ft.colors.WHITE,
                        on_click=lambda e: self.page.go(LOGIN_PAGE_VIEW_URL)
                    )
                ],
                tight=True,
            ),
        )
        self.bgcolor = PastelColors.WHITE_BASE
        self.open = True