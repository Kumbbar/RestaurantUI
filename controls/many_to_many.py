import flet as ft

from core.selection_datatables_list import PermissionsManySelectionsTable, BaseDatatable, \
    UserPermissionsManySelectionsTable
from services.requests import RequestMethod


def get_param_ids(ids):
    return dict(
        ids=','.join(map(str, ids))
    )


class ManyToManyDataControl(ft.UserControl):
    data_table: BaseDatatable
    url: str = '/admin/user_permissions/'

    def __init__(self):
        super().__init__()
        self.value = None
        self.current_obj_data = UserPermissionsManySelectionsTable(autoload=False)
        self.all_data = PermissionsManySelectionsTable()
        self.content = ft.ResponsiveRow(
            controls=[
                ft.Text('PERMISSIONS', col=12, weight=ft.FontWeight.BOLD, size=16),
                ft.Text('ALL', col=6, weight=ft.FontWeight.BOLD, size=16),
                ft.Text('CURRENT', col=6, weight=ft.FontWeight.BOLD, size=16),
                ft.Column(
                    col=6,
                    controls=[
                        self.all_data,
                        ft.ElevatedButton('ADD', on_click=self.add_obj_relation)

                    ],
                ),
                ft.Column(
                    col=6,
                    controls=[
                        self.current_obj_data,
                        ft.ElevatedButton('DELETE', on_click=self.delete_obj_relation)

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

