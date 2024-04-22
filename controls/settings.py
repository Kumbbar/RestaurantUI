import math

import flet_core as ft

from consts.colors import PastelColors
from services.requests import RequestMethod


class SettingsContainer(ft.Container):
    def __init__(self):
        super().__init__()
        self.border_radius = 10
        self.padding = ft.Padding(10, 10, 10, 5)
        self.bgcolor = ft.colors.AMBER_50
        self.alignment = ft.alignment.center
        self.content = ft.Column(
            [
                ft.Text('In development', col=12, weight=ft.FontWeight.BOLD, size=15, text_align=ft.TextAlign.CENTER),
                ft.Icon(ft.icons.SETTINGS, col=12),
                ft.NavigationRail(height=0)
            ],
            alignment=ft.alignment.center
        )
        self.gradient = ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.Alignment(1, 1),
                colors=[
                    PastelColors.SEA_GREEN,
                    PastelColors.SEA_GREEN,
                    PastelColors.VERY_LIGHT_BROWN,
                ],
                tile_mode=ft.GradientTileMode.MIRROR,
                rotation=math.pi / 3,
            )