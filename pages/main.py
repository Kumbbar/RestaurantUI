import math

import flet as ft
from consts.colors import PastelColors
from controls.menu import MainMenu
from core.tiles_list import get_admin_tiles
from pages import BasePage


class MainPage(BasePage):
    def __init__(self, page: ft.Page):
        super().__init__(page)
        self.view_hide_text = ft.Text(
            value='View',
            color=PastelColors.WHITE_BASE,
            font_family='poppins medium',

        )
        self.content = ft.Container(
            alignment=ft.alignment.center,
            height=50, width=150,
            bgcolor='white',
            content=ft.Text(
                value='Get Started',
                size=20,
                color='black'
            )
        )
        self.test = ft.Container(
            bgcolor='green',
            height=300,
            width=300,
        )
        self.workspace = ft.ResponsiveRow(
                                controls=get_admin_tiles()
        )
        self.content = ft.Container(
            padding=ft.Padding(20, 20, 20, 20),
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.Alignment(0.8, 1),
                colors=[
                    PastelColors.LIGHT_BROWN,
                    PastelColors.WHITE_BASE
                ],
                tile_mode=ft.GradientTileMode.MIRROR,
                rotation=math.pi / 3,
            ),
            content=ft.ResponsiveRow(
                controls=[
                    MainMenu(),
                    ft.Container(
                        content=self.workspace,
                        col={"sm": 8, "md": 8, "xl": 8, "xs": 11},
                    )
                ]
            )
        )






