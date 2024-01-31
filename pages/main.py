import math

import flet as ft
from consts.colors import PastelColors
from consts.sizes import BUTTON_HEIGHT
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
            on_click=self.logout_click,
            height=50, width=150,
            bgcolor='white',
            content=ft.Text(
                value='Get Started',
                size=20,
                color='black'
            )
        )
        self.content = ft.ResponsiveRow(
            controls=[
                ft.Container(
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.top_left,
                        end=ft.Alignment(0.8, 1),
                        colors=[
                            "0xff1f005c",
                            "0xff5b0060",
                            "0xff870160",
                            "0xffac255e",
                            "0xffca485c",
                            "0xffe16b5c",
                            "0xfff39060",
                            "0xffffb56b",
                        ],
                        tile_mode=ft.GradientTileMode.MIRROR,
                        rotation=math.pi / 3,
                    ),
                    col={
                        "xs": 0,
                        "sm": 4,
                        "md": 2,
                        "xl": 2
                    },
                    content=ft.NavigationRail(
                        selected_index=0,
                        extended=True,
                        height=800,
                        label_type=ft.NavigationRailLabelType.ALL,
                        leading=ft.Container(
                            content=ft.Icon(
                                name=ft.icons.FAVORITE
                            )
                        ),

                        destinations=[
                            ft.NavigationRailDestination(
                                label='ADMIN',
                                selected_icon=ft.icons.DASHBOARD,
                                icon=ft.icons.DASHBOARD_OUTLINED,
                            ),
                            ft.NavigationRailDestination(
                                label='SETTINGS',
                                selected_icon=ft.icons.SETTINGS,
                                icon=ft.icons.SETTINGS_OUTLINED,
                            ),
                            ft.NavigationRailDestination(
                                label='ABOUT',
                                selected_icon=ft.icons.TAG,
                                icon=ft.icons.TAG_OUTLINED,
                            )

                        ]
                    )
                )
            ]
        )


    def logout_click(self, _):
        self.auth_service.logout_user()
        if not self.auth_service.is_authenticated:
            self.page.go(LOGIN_PAGE_VIEW_URL)

