import flet_core as ft


class CellText(ft.Text):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = ft.colors.BLACK