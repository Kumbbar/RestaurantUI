import flet_core as ft
from pydantic import BaseModel

from controls.bottom_sheets import BottomSheetServiceUnavailable
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


class BaseCreateUpdateDialog(ft.AlertDialog):
    url: str
    pydantic_model: BaseModel
    title = 'Create data'
    fields = {
        'name': ft.TextField(),
        'content_type': ft.TextField(),
        'codename': ft.TextField()
    }

    def __init__(self, id=None):
        if id:
            pass
        super().__init__()
        self.open = True
        self.modal = True
        controls = [ft.Text(self.__class__.title)]
        controls.extend(list(self.__class__.fields.values()))
        self.content = ft.Column(
            width=600,
            controls=controls
        )
        self.actions = [
            ft.TextButton("Save", on_click=self.save_click),
            ft.TextButton("Cancel", on_click=self.no_click),
        ]
        self.actions_alignment = ft.MainAxisAlignment.END

    def save_click(self, _):
        dialog = BottomSheetServiceUnavailable()
        self.page.bottom_sheet = dialog
        self.page.update()

    def no_click(self, _):
        self.open = False
        self.page.update()

