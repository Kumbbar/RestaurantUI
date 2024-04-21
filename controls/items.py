import copy
import time

import flet_core as ft

from consts.colors import PastelColors


class NavigationTile(ft.UserControl):
    title: str = 'UNSET'
    icon: str = ft.icons.ERROR
    open: str = ft.icons.ERROR

    def __init__(self, title: str, icon: str, next_control=None):
        super().__init__()
        self.__next_control = next_control
        self.content = ft.Container(
            height=0,
            col={"sm": 0, "md": 0, "xl": 0, "xs": 0},
            animate=ft.animation.Animation(500, ft.AnimationCurve.BOUNCE_OUT),
            margin=ft.Margin(10, 0, 0, 0),
            on_click=self.tile_click,
            border_radius=10,
            padding=ft.Padding(10, 10, 10, 0),
            bgcolor=PastelColors.SEA_GREEN,
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text(
                        title,
                        text_align=ft.TextAlign.CENTER
                    ),
                    ft.Icon(name=icon)
                ]
            )

        )

    def tile_click(self, _):
        self.page.current_view.workspace.controls.clear()
        self.page.current_view.workspace.controls.append(self.__next_control)
        self.page.update()

    def build(self):
        return self.content

    def did_mount(self):
        time.sleep(0.03)
        self.content.height = 100
        self.content.col = {"sm": 8, "md": 8, "xl": 8, "xs": 2},
        self.update()


class CustomWidthNavigationTile(NavigationTile):
    def __init__(self, title: str, icon: str, next_control=None, width=None):
        super().__init__(title, icon, next_control)
        self.content.bgcolor = PastelColors.LIGHT_BROWN
        if width:
            self.content.width = width
