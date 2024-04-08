import flet as ft

from consts.colors import PastelColors
from settings import BACKEND_BASE_URL


class CreateMenuTemplate(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.value = None
        self.dish_types_order = ft.TextField(label='dish types ids',
                                             hint_text='For example 4,2,6,1. Menu will start from 4 to 1', col=8,
                                             height=40)
        self.create_menu_button = ft.ElevatedButton(
                        'CREATE',
                        bgcolor=PastelColors.LIGHT_BROWN,
                        color=ft.colors.WHITE,
                        on_click=self.create_menu_click,
                        col=4
                    )
        self.content = ft.ResponsiveRow(
            [
                ft.Text('CREATE MENU TEMPLATE', col=12, size=15, weight=ft.FontWeight.BOLD),
                self.dish_types_order,
                self.create_menu_button
            ]
        )

    def build(self):
        return self.content

    def create_menu_click(self, _):
        self.page.launch_url(f'{BACKEND_BASE_URL}/render_menu/{self.value}/?order={self.dish_types_order.value}')