import flet as ft

from core.selection_datatables_list import PermissionsManySelectionsTable
from data_models import BaseDataModel


class Test(ft.UserControl):
    name: str
    data_model: BaseDataModel

    def __init__(self):
        super().__init__()
        self.value = None

        self.content = ft.ResponsiveRow(
            controls=[
                ft.Column(col=6, controls=[PermissionsManySelectionsTable()]),
                ft.Column(col=6, controls=[PermissionsManySelectionsTable()])
            ]
        )

    def build(self):
        return self.content

