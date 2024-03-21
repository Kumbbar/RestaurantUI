from typing import List

import flet as ft

from controls.dialogs import DatatableDeleteDialog, BaseCreateUpdateDialog
from controls.text import CellText
from data_models import BaseDataModel
from styles.buttons import CreateDataTableButton


class BaseDatatable(ft.UserControl):
    visible_columns: List
    data_model: BaseDataModel

    def __init__(self, extra_url='', autoload=True):
        super().__init__()
        self.extra_url = extra_url
        self.autoload = autoload
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
        self.header_navigation = []
        self.content = self.create_content()

    def build(self):
        return self.content

    def did_mount(self):
        if self.autoload:
            self.refresh_data()
        self.resize()

    def create_content(self):
        return ft.Container(
            col={"sm": 8, "md": 8, "xl": 8, "xs": 11}, height=0,
            padding=ft.padding.Padding(0, 0, 0, 0),
            animate=ft.animation.Animation(300, ft.AnimationCurve.EASE_IN),
            content=ft.Column(
                on_scroll_interval=0,
                controls=[
                    ft.ResponsiveRow(
                        controls=self.header_navigation,
                        alignment=ft.MainAxisAlignment.START
                    ),
                    ft.ListView(
                        expand=1,
                        spacing=10,
                        height=100,
                        controls=[
                            self.datatable
                        ]
                    )
                ]
            )
        )

    def refresh_data(self):
        self.datatable.rows = self.get_data()
        self.datatable.columns = self.get_columns()
        self.datatable.update()

    def resize(self):
        if self.page.width / self.page.height > 4/3:
            self.content.height = self.page.height * 0.8
        else:
            self.content.height = self.page.height * 0.4
        self.content.update()

    def get_columns(self):
        columns = [
            ft.DataColumn(
                CellText(key)
            ) for key in self.__class__.visible_columns
        ]
        return columns

    def get_params_for_request(self):
        return dict()

    def get_data(self):
        request_data = dict(params=self.get_params_for_request())
        self.data = self.__class__.data_model(self.page, self.extra_url, **request_data)
        rows = self.convert_to_datatable_rows()
        return rows

    def get_row_template(self, row):
        return ft.DataRow(cells=[], data=row.id)

    def convert_to_datatable_rows(self):
        result_rows = []
        for row in self.data.result_list:
            data_row = self.get_row_template(row)
            if not self.row_filter(data_row):
                continue
            for key in self.__class__.visible_columns:
                data_row.cells.append(
                    ft.DataCell(
                        CellText(getattr(row, key)),
                        data=row.id,
                    )
                )
            result_rows.append(data_row)
        return result_rows

    def row_filter(self, row) -> bool:
        return True


class ManySelectionsMixinDatatable(object):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.datatable.show_checkbox_column = True

    def get_row_template(self, row):
        return ft.DataRow(cells=[], on_select_changed=self.change_row_select, data=row.id)

    def change_row_select(self, e):
        e.control.selected = not e.control.selected
        e.control.update()

    @property
    def selected_ids(self):
        return [row.data for row in self.datatable.rows if row.selected]

    @property
    def all_ids(self):
        return [row.data for row in self.datatable.rows]


class ExcludeIdsMixinDatatable(object):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.exclude_ids = []

    def row_filter(self, row) -> bool:
        if row.data in self.exclude_ids:
            return False
        return True

    def get_params_for_request(self):
        result = super().get_params_for_request()
        result['page_size'] = 100000
        return result


class SearchMixinDatatable(object):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.search_field = ft.TextField(
            label='SEARCH',
            height=30,
            text_size=14,
            content_padding=ft.Padding(10, 0, 0, 0),
            col={"xs": 7, "sm": 7, "lg": 4, "xl": 4}
        )
        self.refresh_button = ft.IconButton(
            icon=ft.icons.REFRESH_ROUNDED,
            on_click=self.refresh_data_click,
            icon_color=ft.colors.BLACK,
            tooltip='refresh',
            col={"xs": 2, "sm": 2, "lg": 1, "xl": 1}
        )
        self.header_navigation.extend([self.search_field, self.refresh_button])
        self.create_content()

    def get_params_for_request(self):
        result = dict()
        result['search'] = self.search_field.value
        return result

    def refresh_data_click(self, e):
        self.refresh_data()
        self.resize()


class PydanticDatatable(SearchMixinDatatable, BaseDatatable):
    foreign_data_template = dict()
    dialog: BaseCreateUpdateDialog
    url: str

    def __init__(self):
        super().__init__()
        print(self.__class__.__mro__, 'ykras')
        self.foreign_data = dict()
        self.create_button = ft.OutlinedButton(
            'CREATE',
            style=CreateDataTableButton(),
            on_click=self.show_create_dialog,
            col={"xs": 5, "sm": 4, "lg": 3, "xl": 2}
        )
        self.header_navigation.insert(0, self.create_button)
        self.content = self.create_content()

    def refresh_data(self):
        self.datatable.rows = self.get_data()
        self.datatable.columns = self.get_columns()
        self.datatable.update()

    def get_columns(self):
        columns = [
            ft.DataColumn(
                CellText(key)
            ) for key in self.__class__.visible_columns
        ]
        columns.append(
            ft.DataColumn(CellText('action'))
        )
        return columns

    def get_data(self):
        request_data = dict(params=self.get_params_for_request())
        self.data = self.__class__.data_model(self.page, **request_data)
        self.__get_foreign_data()
        rows = self.convert_to_datatable_rows()
        return rows

    def get_params_for_request(self):
        result = dict()
        result['search'] = self.search_field.value
        return result

    def __get_foreign_data(self):
        for key, value in self.__class__.foreign_data_template.items():
            self.foreign_data[key] = value(self.page)

    def convert_to_datatable_rows(self):
        result_rows = []
        for row in self.data.result_list:
            data_row = self.get_row_template(row)

            for key in self.__class__.visible_columns:
                if key in self.foreign_data.keys():
                    data_row.cells.append(
                        ft.DataCell(
                            CellText(self.foreign_data[key].foreign_data[getattr(row, key)]),
                            data=row.id,
                            on_double_tap=self.obj_event
                        )
                    )
                else:
                    data_row.cells.append(
                        ft.DataCell(
                            CellText(getattr(row, key)),
                            data=row.id,
                            on_double_tap=self.obj_event
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

    def obj_event(self, e):
        update_dialog = self.__class__.dialog(e.control.data)
        self.page.dialog = update_dialog
        self.page.update()

    def show_delete_dialog(self, e):
        self.page.dialog = DatatableDeleteDialog(e.control.data, self)
        self.page.update()


def test(e):
    e.control.selected = not e.control.selected
    e.control.update()
