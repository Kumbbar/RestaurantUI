import math

import flet_core as ft

from consts.colors import PastelColors
from services.requests import RequestMethod


class InformationPanel(ft.Container):
    def __init__(self):
        super().__init__()
        self.col = 12
        self.border_radius = 10
        self.padding = ft.Padding(10, 10, 10, 5)
        self.bgcolor = ft.colors.AMBER_50
        self.running = True
        self.tables_reserved_label = ft.Text()
        self.orders_label = ft.Text(col=6)
        self.refresh_btn = ft.IconButton(ft.icons.REFRESH, col=6, on_click=self.update_info)
        self.content = ft.Column(
            [
                ft.Row([ft.Text('Today information', col=6, weight=ft.FontWeight.BOLD, size=14), self.refresh_btn]),
                self.tables_reserved_label,
                self.orders_label,
                ft.NavigationRail(height=0)
            ],
        )
        self.gradient = ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.Alignment(1, 1),
                colors=[
                    PastelColors.VERY_LIGHT_BROWN,
                    PastelColors.VERY_LIGHT_BROWN,
                    PastelColors.SEA_GREEN,
                    PastelColors.SEA_GREEN,
                ],
                tile_mode=ft.GradientTileMode.MIRROR,
                rotation=math.pi / 3,
            )

    def did_mount(self):
        self.update_info(None)

    def update_info(self, _):
        response = self.page.current_view.auth_service.send_closed_request(
            RequestMethod.GET,
            f'/food/today_restaurant_info/',
        )
        if not response.ok:
            return
        response_data = response.json()
        self.tables_reserved_label.value = f'Tables reserved: {response_data['tables_reserved']}'
        self.orders_label.value = f'Not ready orders: {response_data['not_ready_orders']}'
        self.tables_reserved_label.update()
        self.orders_label.update()
