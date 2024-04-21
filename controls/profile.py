import math

import flet as ft

from consts.colors import PastelColors


class SmallProfileContainer(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.first_name = 'Unknown'
        self.last_name = 'Unknown'

        self.text = ft.Text(f'{self.first_name} {self.last_name}', size=15, weight=ft.FontWeight.BOLD)
        self.content = ft.Container(
            height=36,
            content=ft.Row(
                controls=[
                    ft.Container(
                        content=self.text,
                        margin=ft.Margin(0, 0, 5, 0),
                        padding=ft.Padding(0, 0, 0, 0)
                    ),
                    ft.Container(
                        ft.Icon(
                            ft.icons.PERSON_2
                        ),
                        margin=ft.Margin(0, 0, 10, 0),
                        padding=ft.Padding(0, 0, 0, 0)
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
                    PastelColors.VERY_LIGHT_BROWN,
                    PastelColors.SEA_GREEN,
                    PastelColors.SEA_GREEN,
                ],
                tile_mode=ft.GradientTileMode.MIRROR,
                rotation=math.pi / 3,
            ),
            border_radius=10,
            margin=ft.Margin(10, 0, 0, 0),
            bgcolor=ft.colors.BLACK
        )

    def build(self):
        return self.content

    def get_names(self):
        self.first_name = self.page.current_view.current_user.data.first_name
        self.last_name = self.page.current_view.current_user.data.last_name

    def set_names(self):
        self.text.value = f'{self.first_name} {self.last_name}'

    def did_mount(self):
        self.get_names()
        if self.first_name != 'Unknown' and self.last_name != 'Unknown':
            self.set_names()
        self.update()
