import flet_core as ft

from consts.colors import PastelColors
from settings import LOGIN_PAGE_VIEW_URL, SESSION_TOKEN_KEY


class BottomSheetServiceUnavailable(ft.BottomSheet):
    def __init__(self):
        super().__init__()
        self.content = ft.Container(
            padding=ft.Padding(20, 10, 20, 10),
            width=500,
            content=ft.Column(
                [
                    ft.Text("Server unavailable 500", size=18, weight=ft.FontWeight.BOLD),
                    ft.Text("Contact to developers if you need", size=14),
                ],
                tight=True,
            ),
        )
        self.bgcolor = PastelColors.BROWN_RED
        self.open = True


class BottomSheetOrderTotalPrice(ft.BottomSheet):
    def __init__(self, price):
        super().__init__()
        self.content = ft.Container(
            padding=ft.Padding(20, 10, 20, 10),
            width=500,
            content=ft.Column(
                [
                    ft.Text(f"TOTAL PRICE - {price}", size=18, weight=ft.FontWeight.BOLD),
                ],
                tight=True,
                height=60
            ),
        )
        self.bgcolor = PastelColors.LIGHT_BROWN
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
                        on_click=self.login_redirect
                    )
                ],
                tight=True,
            ),
        )
        self.bgcolor = PastelColors.WHITE_BASE
        self.open = True

    def login_redirect(self, _):
        self.page.current_view.auth_service.delete_exists_user_token()
        self.page.go(LOGIN_PAGE_VIEW_URL)


class ExceptionBottomSheet(ft.BottomSheet):
    def __init__(self, data: dict):
        super().__init__()
        self.content = ft.Container(
            padding=ft.Padding(20, 10, 20, 10),
            width=500,
            content=ft.Column(
                controls=self.convert_data(data),
                tight=True
            ),
        )
        self.bgcolor = PastelColors.WHITE_BASE
        self.open = True

    def convert_data(self, data):
        result = []
        for key, value in data.items():
            key_result = []
            if isinstance(value, list):
                for data in value:
                    key_result.append(str(data))
                total_key_result = ',  '.join(key_result)
            else:
                total_key_result = value
            result.append(
                ft.Text(
                    value=f'{key} - {total_key_result}',
                    size=14
                )
            )
        return result


class BottomSheetDefaultWorkspace(ft.BottomSheet):
    def __init__(self, workspace_name):
        super().__init__()
        self.content = ft.Container(
            padding=ft.Padding(20, 10, 20, 10),
            width=500,
            content=ft.Column(
                [
                    ft.Text(f"DEFAULT WORKSPACE - {workspace_name}", size=18, weight=ft.FontWeight.BOLD),
                ],
                tight=True,
                height=40
            ),
        )
        self.bgcolor = PastelColors.LIGHT_BROWN
        self.open = True