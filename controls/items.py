import flet_core as ft


class NavigationTile(ft.Container):
    title: str = 'UNSET'
    icon: str = ft.icons.ERROR
    open: str = ft.icons.ERROR

    def __init__(self, title: str, icon: str, next_control=None):
        super().__init__()
        self.__next_control = next_control
        self.content = ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text(
                    title,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Icon(name=icon)
            ]
        )
        self.margin = ft.Margin(10, 0, 0, 0)
        self.on_click = self.tile_click
        self.height = 100
        self.width = 300
        self.border_radius = 10
        self.padding = ft.Padding(10, 10, 10, 0)
        self.bgcolor = 'red'
        self.col = {"sm": 6, "md": 4, "xl": 2}

    def tile_click(self, _):
        self.page.current_view.workspace.controls.clear()
        self.page.current_view.workspace.controls.append(self.__next_control)
        self.page.update()


