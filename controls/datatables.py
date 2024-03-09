from typing import List, Dict

import flet as ft

from controls.dialogs import DatatableDeleteDialog, BaseCreateUpdateDialog
from controls.text import CellText
from data_models import BaseDataModel
from data_models.dict_model import DictDataModeL
from styles.buttons import CreateDataTableButton


class PydanticDatatable(ft.Container):
    visible_columns: List
    foreign_data_template = dict()
    data_model: BaseDataModel
    dialog: BaseCreateUpdateDialog
    url: str

    def __init__(self):
        super().__init__()
        self.datatable = ft.DataTable(
            col={"sm": 10, "md": 10, "xl": 10, "xs": 10},
            bgcolor="white",
            border=ft.border.all(1.5, "black"),
            border_radius=10,
            vertical_lines=ft.border.BorderSide(1.5, "black"),
            horizontal_lines=ft.border.BorderSide(1, "black"),
            sort_column_index=0,
            heading_row_color=ft.colors.BLACK12,
            heading_row_height=50,
            data_row_min_height=40,
            data_row_max_height=40,
            divider_thickness=0,
            column_spacing=10,
        )
        self.foreign_data = dict()
        self.refresh_button = ft.IconButton(
            icon=ft.icons.REFRESH_ROUNDED,
            on_click=self.refresh_data_click,
            icon_color=ft.colors.BLACK,
            tooltip='refresh'
        )
        self.create_button = ft.OutlinedButton(
            'CREATE',
            style=CreateDataTableButton(),
            on_click=self.show_create_dialog
        )
        self.content = (
            ft.Container(
                padding=ft.padding.Padding(0, 0, 0, 0),
                content=ft.Column(

                    on_scroll_interval=0,
                    controls=[
                        ft.Row(

                            controls=[
                                self.create_button,
                                self.refresh_button,
                            ],
                            alignment=ft.MainAxisAlignment.START
                        ),

                        ft.ListView(
                            expand=1,
                            spacing=10,
                            controls=[
                                self.datatable
                            ]
                        )
                    ]

                )
            )
        )

    def refresh_data_click(self, e):
        self.refresh_data()

    def refresh_data(self):
        self.datatable.rows = self.__get_data()
        self.datatable.columns = self.__get_columns()
        self.datatable.update()

    def __get_columns(self):
        columns = [
            ft.DataColumn(
                CellText(key)
            ) for key in self.__class__.visible_columns
        ]
        columns.append(
            ft.DataColumn(CellText('action'))
        )
        return columns

    def __get_data(self):
        self.data = self.__class__.data_model(self.page)
        self.__get_foreign_data()
        rows = self.__convert_to_datatable_rows()
        return rows

    def __get_foreign_data(self):
        for key, value in self.__class__.foreign_data_template.items():
            self.foreign_data[key] = value(self.page)

    def __convert_to_datatable_rows(self):
        result_rows = []
        for row in self.data.result_list:
            data_row = ft.DataRow(cells=[])
            for key in self.__class__.visible_columns:
                if key in self.foreign_data.keys():
                    data_row.cells.append(
                        ft.DataCell(
                            CellText(self.foreign_data[key].foreign_data[getattr(row, key)]),
                            data=row.id,
                            on_double_tap=self.show_update_dialog
                        )
                    )
                else:
                    data_row.cells.append(
                        ft.DataCell(
                            CellText(getattr(row, key)),
                            data=row.id,
                            on_double_tap=self.show_update_dialog
                        )
                    )
            data_row.cells.append(
                ft.DataCell(
                    ft.IconButton(
                        ft.icons.DELETE,
                        icon_color=ft.colors.RED_500,
                        data=row.id,
                        on_click=self.show_delete_dialog,
                        tooltip='delete'
                    )
                )
            )
            result_rows.append(data_row)
        return result_rows

    def show_create_dialog(self, _):
        create_dialog = self.__class__.dialog()
        self.page.dialog = create_dialog
        self.page.update()

    def show_update_dialog(self, e):
        create_dialog = self.__class__.dialog(e.control.data)
        self.page.dialog = create_dialog
        self.page.update()

    def show_delete_dialog(self, e):
        self.page.dialog = DatatableDeleteDialog(e.control.data, self)
        self.page.update()

