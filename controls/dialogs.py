import copy
from abc import ABC, abstractmethod
from typing import List, Dict

import flet_core as ft
from flet_core import UserControl, TextField
from flet_core.form_field_control import FormFieldControl
from pydantic import BaseModel

from controls.bottom_sheets import BottomSheetServiceUnavailable
from controls.dropdown import CustomDropDown
from controls.file_pickers import FilePickerImage, FileField
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


class BaseCreateUpdateDialog(ABC, ft.UserControl):
    url: str

    @abstractmethod
    def get_fields(self) -> dict[str, TextField | CustomDropDown]:
        pass

    def get_extra_controls(self):
        return {}

    def __init__(self, datatable, id=''):
        super().__init__()
        self.id = id
        self.datatable_ref = datatable
        self.fields = self.get_fields()
        self.extra_controls = self.get_extra_controls()

        controls = list(self.fields.values())
        extra_controls = list(self.extra_controls.values())
        controls.extend(
            extra_controls
        )
        content = ft.Column(
            width=900,
            controls=controls,
            scroll=ft.ScrollMode.AUTO
        )
        if id:
            title = ft.Text(f'Update {id}', weight=ft.FontWeight.BOLD)
        else:
            title = ft.Text(f'Create', weight=ft.FontWeight.BOLD)

        self.actions = [
            ft.TextButton("Save and close", on_click=self.save_click),
            ft.TextButton("Save", on_click=self.save_not_close_click),
            ft.TextButton("Cancel", on_click=self.no_click),
        ]
        self.actions_alignment = ft.MainAxisAlignment.END

        self.content = ft.AlertDialog(
            title=title,
            modal=True,
            open=True,
            actions=self.actions,
            content=content,
            actions_alignment=self.actions_alignment,

        )

    def did_mount(self):
        if self.id:
            json_data = self.get_data()
            self.set_fields_data(json_data)

            self.set_extra_controls()
            self.update()

    def set_extra_controls(self):
        for key in self.extra_controls.keys():
            self.extra_controls[key].value = self.id
            self.extra_controls[key].update()

    def set_fields_data(self, data):
        for key in self.fields.keys():
            self.fields[key].value = data.get(key)
            self.fields[key].update()

    def get_fields_data(self):
        result = {}
        for key in self.fields.keys():
            if isinstance(self.fields[key], FileField):
                continue
            result[key] = self.fields[key].value
        return result

    def get_files_data(self):
        result = {}
        for key in self.fields.keys():
            if isinstance(self.fields[key], FileField) and getattr(self.fields[key], 'file_changed') is True:
                result[key] = open(self.fields[key].value, 'rb')
        return result

    def send_fields_data(self):
        fields_data = self.get_fields_data()
        files_data = self.get_files_data()
        if self.id:
            id_url = f'{self.id}/'
            method = RequestMethod.PUT
        else:
            id_url = ''
            method = RequestMethod.POST

        response = self.page.current_view.auth_service.send_closed_request(
            method,
            f'{self.__class__.url}{id_url}',
            data=fields_data,
            files=files_data
        )
        return response

    def get_data(self):
        response = self.page.current_view.auth_service.send_closed_request(
            RequestMethod.GET,
            f'{self.__class__.url}{self.id}/'
        )
        if response.ok:
            return response.json()

    def build(self):
        return self.content

    def save_click(self, _):
        response = self.send_fields_data()
        if response.ok:
            self.datatable_ref.refresh_data()
            self.close()

    def save_not_close_click(self, _):
        response = self.send_fields_data()
        if response.ok:
            self.id = response.json().get('id')
            self.did_mount()
            self.datatable_ref.refresh_data()

    def no_click(self, _):
        self.close()

    def close(self):
        self.content.open = False
        self.update()


