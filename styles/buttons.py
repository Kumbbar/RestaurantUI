import flet_core as ft
from consts.colors import PastelColors


class CreateDataTableButton(ft.ButtonStyle):
    def __init__(self):
        self.color = ft.colors.BLACK
        self.bgcolor = PastelColors.LIGHT_BROWN
