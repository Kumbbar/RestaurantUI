import flet_core as ft

from consts.colors import PastelColors


class BottomSheetServiceUnavailable(ft.BottomSheet):
    def __init__(self):
        super().__init__()
        self.content = ft.Container(
            padding=ft.Padding(20, 10, 20, 10),
            width=500,
            content=ft.Column(
                [
                    ft.Text("Server unavailable", size=18, weight=ft.FontWeight.BOLD),
                    ft.Text("Contact to developers if you need", size=14),
                ],
                tight=True,
            ),
        )
        self.bgcolor = PastelColors.BROWN_RED
        self.open = True
