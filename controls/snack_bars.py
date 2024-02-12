import flet_core as ft
from flet_core import Control


class SnackBarDatatableDelete(ft.SnackBar):
    def __init__(self, id):
        text = ft.Text(f'Data {id} successfully deleted', size=20, color=ft.colors.WHITE)
        super().__init__(text)
        self.bgcolor = ft.colors.RED_ACCENT_200
        self.open = True

