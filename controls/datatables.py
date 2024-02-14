import flet as ft
from pydantic import BaseModel
import json

from controls.dialogs import DatatableDeleteDialog, BaseCreateUpdateDialog
from controls.text import CellText
from services.requests.auth import RequestMethod
from styles.buttons import CreateDataTableButton


class PydanticDatatable(ft.Container):
    table_pydantic_model: BaseModel
    table_response_model: BaseModel
    edit_form_pydantic_model: BaseModel
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
        self.refresh_button = ft.IconButton(
            icon=ft.icons.REFRESH_ROUNDED,
            on_click=self.refresh_data_click,
            icon_color=ft.colors.BLACK,
            tooltip='refresh'
        )
        self.test_dialog = BaseCreateUpdateDialog()
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

    def show_create_dialog(self, _):
        self.test_dialog.open = True
        self.page.dialog = self.test_dialog
        self.page.update()

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
            ) for key in self.__class__.table_pydantic_model.model_fields.keys()
        ]
        columns.append(
            ft.DataColumn(CellText('action'))
        )
        return columns

    def __get_data(self):
        try:
            pydantic_response = self.__get_pydantic_response()
        except ConnectionError:
            return list()
        rows = self.__convert_to_datatable_rows(pydantic_response)
        return rows

    def __get_pydantic_response(self):
        response = self.page.current_view.auth_service.send_closed_request(
            RequestMethod.GET,
            self.__class__.url
        )
        if not response.ok:
            raise ConnectionError
        data = self.__validate_response(response)
        return data

    def __validate_response(self, response):
        return self.__class__.table_response_model.model_validate_json(
            json.dumps(response.json())
        )

    def __convert_to_datatable_rows(self, response):
        result_rows = []
        for row in response.results:
            data_row = ft.DataRow(cells=[])
            for key in self.__class__.table_pydantic_model.model_fields.keys():
                data_row.cells.append(
                    ft.DataCell(
                        CellText(getattr(row, key)),
                        data=row.id
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

    def show_delete_dialog(self, e):
        self.page.dialog = DatatableDeleteDialog(e.control.data, self)
        self.page.update()

