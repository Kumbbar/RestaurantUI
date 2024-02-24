import copy

import flet_core as ft
from pydantic import BaseModel

from controls.bottom_sheets import BottomSheetServiceUnavailable
from controls.dropdown import CustomDropDown
from controls.snack_bars import SnackBarDatatableDelete
from services.requests import RequestMethod
from settings import BACKEND_LOGIN_PATH


class LogoutDialog(ft.AlertDialog):
    def __init__(self, logout_event):
        super().__init__()
        self.open = True
        self.modal = True
        self.logout_event = logout_event
        self.content = ft.Text("Do you really want to log out?")
        self.actions = [
            ft.TextButton("Yes", on_click=self.logout_event),
            ft.TextButton("No", on_click=self.no_click),
        ]
        self.actions_alignment = ft.MainAxisAlignment.END

    def no_click(self, _):
        self.open = False
        self.page.update()


class DatatableDeleteDialog(ft.AlertDialog):
    def __init__(self, id, datatable_ref):
        super().__init__()
        self.datatable_ref = datatable_ref
        self.open = True
        self.modal = True
        self.item_id = id
        self.content = ft.Text(f"Do you really want to delete {id}?")
        self.actions = [
            ft.TextButton("Yes", on_click=self.delete_item),
            ft.TextButton("No", on_click=self.no_click),
        ]
        self.actions_alignment = ft.MainAxisAlignment.END

    def delete_item(self, e):
        response = self.page.current_view.auth_service.send_closed_request(
            RequestMethod.DELETE,
            f'{self.datatable_ref.__class__.url}{self.item_id}/'
        )
        if response.ok:
            self.open = False
            self.page.snack_bar = SnackBarDatatableDelete(self.item_id)
            self.datatable_ref.refresh_data()
        self.page.update()

    def no_click(self, _):
        self.open = False
        self.page.update()


class BaseCreateUpdateDialog(ft.UserControl):
    url: str = '/admin/permissions/'
    fields = {
        'name': ft.TextField(label='name'),
        'content_type': CustomDropDown(),
        'codename': ft.TextField(label='codename')
    }

    def __init__(self, id=''):
        super().__init__()
        self.id = id

        self.fields = copy.deepcopy(self.__class__.fields)
        controls = list(self.fields.values())

        self.content = ft.Column(
            width=600,
            controls=controls
        )
        if id:
            title = ft.Text(f'Update {id}', weight=ft.FontWeight.BOLD)
        else:
            title = ft.Text(f'Create', weight=ft.FontWeight.BOLD)

        self.actions = [
            ft.TextButton("Save", on_click=self.save_click),
            ft.TextButton("Cancel", on_click=self.no_click),
        ]
        self.actions_alignment = ft.MainAxisAlignment.END

        self.content = ft.AlertDialog(
            title=title,
            modal=True,
            open=True,
            actions=self.actions,
            content=self.content,
            actions_alignment=self.actions_alignment,

        )

    def did_mount(self):
        if self.id:
            json_data = self.get_data()
            self.set_fields_data(json_data)

    def set_fields_data(self, data):
        for key in self.fields.keys():
            if hasattr(self.fields[key], 'content'):
                self.fields[key].content.value = data.get(key)
            else:
                self.fields[key].value = data.get(key)

    def get_fields_data(self):
        result = {}
        for key in self.fields.keys():
            result[key] = self.fields[key].value
        return result

    def send_fields_data(self):
        fields_data = self.get_fields_data()
        if self.id:
            id_url = f'{self.id}/'
            method = RequestMethod.PUT
        else:
            id_url = ''
            method = RequestMethod.POST

        response = self.page.current_view.auth_service.send_closed_request(
            method,
            f'{self.__class__.url}{id_url}',
            json=fields_data
        )
        if response.ok:
            self.close()

    def get_data(self):
        response = self.page.current_view.auth_service.send_closed_request(
            RequestMethod.GET,
            f'{self.__class__.url}{self.id}'
        )
        if response.ok:
            return response.json()

    def build(self):
        return self.content

    def save_click(self, _):
        self.send_fields_data()
        self.close()

    def no_click(self, _):
        self.close()

    def close(self):
        self.content.open = False
        self.update()


