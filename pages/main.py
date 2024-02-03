import math

import flet as ft
from consts.colors import PastelColors
from consts.sizes import BUTTON_HEIGHT
from controls.menu import MainMenu
from pages import BasePage
from settings import LOGIN_PAGE_VIEW_URL


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
        self.first = ft.Container(
                            height=300,
                            width=700,
                            bgcolor='red',
                            col={"sm": 6, "md": 4, "xl": 2},
            content=ft.Text('first')
                        )
        self.second = ft.Container(
                            height=300,
                            width=300,
                            bgcolor='red',
                            col={"sm": 6, "md": 4, "xl": 2},
            content=ft.Text('second')

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
                    ft.Column(
                        col={"sm": 8, "md": 6, "xl": 6, "xs": 11},
                        scroll=ft.ScrollMode.AUTO,
                        controls=[
                            ft.ResponsiveRow(
                                controls=[
                                    self.first,
                                    self.second,
                                    self.second,
                                    self.second,
                                    self.second,

                                ]
                            )
                        ]

                    )

                ]
            )
        )




