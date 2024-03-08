import math

import flet as ft
from consts.colors import PastelColors
from controls.menu import MainMenu
from core.tiles_list import get_admin_tiles
from pages import BasePage


class MainPage(BasePage):
    def __init__(self, page: ft.Page):
        super().__init__(page)
        print(page, 'jaga')
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
            controls=[]
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
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Column(
                        controls=[
                            MainMenu(),
                            ft.Container(
                                height=100,
                                bgcolor=ft.colors.AMBER_50
                            )
                        ],
                        col={
                            "xs": 12,
                            "sm": 3.8,
                            "md": 3,
                            "xl": 3
                        }
                    ),
                    ft.Column(
                        controls=[
                            ft.Container(
                                height=36,

                                content=ft.Row(
                                    controls=[
                                        ft.Container(
                                            content=ft.Text('Sergei Shtro', size=15, weight=ft.FontWeight.BOLD),
                                            margin=ft.Margin(0, 0, 20, 0),
                                            padding=ft.Padding(0, 0, 0, 0)

                                        ),
                                        ft.Icon(
                                            ft.icons.PERSON_3
                                        )
                                    ],
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                    alignment=ft.MainAxisAlignment.END,


                                ),
                                col={"sm": 8, "md": 10, "xl": 10, "xs": 11},
                                gradient=ft.LinearGradient(
                                    begin=ft.alignment.top_left,
                                    end=ft.Alignment(0.8, 1),
                                    colors=[
                                        "0xffac255e",
                                        "0xffca485c",
                                        "0xffe16b5c",
                                        "0xfff39060",
                                        "0xffffb56b",
                                        PastelColors.MEDIUM_BROWN,
                                    ],
                                    tile_mode=ft.GradientTileMode.MIRROR,
                                    rotation=math.pi / 3,
                                ),
                                border_radius=10,
                                margin=ft.Margin(10, 0, 0, 0),
                                bgcolor=ft.colors.BLACK
                            ),
                            self.workspace
                        ],
                        col={"sm": 8, "md": 8, "xl": 8, "xs": 11}
                    )
                ]
            )
        )






