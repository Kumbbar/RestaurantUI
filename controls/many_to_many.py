import flet as ft

from core.selection_datatables_list import PermissionsManySelectionsTable, BaseDatatable, \
    UserPermissionsManySelectionsTable
from services.requests import RequestMethod


def get_param_ids(ids):
    return dict(
        ids=','.join(map(str, ids))
    )


class ManyToManyDataControl(ft.UserControl):
    all_data_table: BaseDatatable
    current_data_table: BaseDatatable
    url: str

    def __init__(self, label_text):
        super().__init__()
        self.value = None
        self.current_obj_data = self.__class__.current_data_table(autoload=False)
        self.all_data = self.__class__.all_data_table()
        self.content = ft.ResponsiveRow(
            controls=[
                ft.Text(label_text, col=12, weight=ft.FontWeight.BOLD, size=16),
                ft.Text('ALL', col=6, weight=ft.FontWeight.BOLD, size=16),
                ft.Text('CURRENT', col=6, weight=ft.FontWeight.BOLD, size=16),
                ft.Column(
                    col=6,
                    controls=[
                        ft.ElevatedButton('ADD', on_click=self.add_obj_relation),
                        self.all_data,
                    ],
                ),
                ft.Column(
                    col=6,
                    controls=[
                        ft.ElevatedButton('DELETE', on_click=self.delete_obj_relation),
                        self.current_obj_data,
                    ]
                )
            ]
        )

    def delete_obj_relation(self, _):
        params = get_param_ids(self.current_obj_data.selected_ids)
        request_data = dict(params=params)
        response = self.page.current_view.auth_service.send_closed_request(
            RequestMethod.DELETE,
            f'{self.__class__.url}{self.value}/',
            **request_data
        )
        if response.ok:
            self.refresh_tables()

    def add_obj_relation(self, _):
        params = get_param_ids(self.all_data.selected_ids)
        request_data = dict(params=params)
        response = self.page.current_view.auth_service.send_closed_request(
            RequestMethod.POST,
            f'{self.__class__.url}{self.value}/',
            **request_data
        )
        if response.ok:
            self.refresh_tables()

    def build(self):
        return self.content

    def update(self):
        self.current_obj_data.extra_url = self.value
        self.current_obj_data.refresh_data()
        self.all_data.exclude_ids = self.current_obj_data.all_ids
        super().update()

    def refresh_tables(self):
        self.current_obj_data.refresh_data()
        self.all_data.exclude_ids = self.current_obj_data.all_ids
        self.all_data.refresh_data()

