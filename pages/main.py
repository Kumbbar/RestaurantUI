import math
import time

import flet as ft
from consts.colors import PastelColors
from controls.information_panel import InformationPanel
from controls.menu import MainMenu
from controls.profile import SmallProfileContainer
from core.data_models_list import UserProfileDataModel
from pages import BasePage


class MainPage(BasePage):
    def __init__(self, page: ft.Page):
        super().__init__(page)
        self.current_user = self.get_user_data()
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
        self.main_menu = MainMenu()
        self.workspace = ft.ResponsiveRow(
            controls=[],
            col={"sm": 8, "md": 8, "xl": 8, "xs": 11}
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
                            self.main_menu,
                            InformationPanel()
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
                            SmallProfileContainer(),
                            self.workspace,
                        ],
                        col={"sm": 8, "md": 8, "xl": 8, "xs": 11}
                    )
                ]
            )
        )

    def get_user_data(self):
        current_user = None
        while not current_user:
            try:
                current_user = UserProfileDataModel(self.page)
            except ConnectionError:
                time.sleep(2)
        return current_user




