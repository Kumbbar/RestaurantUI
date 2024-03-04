from flet_core import NumbersOnlyInputFilter

from controls.dialogs import BaseCreateUpdateDialog
from controls.dropdown import CustomDropDown
import flet_core as ft


class UsersCreateUpdateDialog(BaseCreateUpdateDialog):
    url = '/admin/users/'

    def get_fields(self):
        return {
            'username': ft.TextField(label='username'),
            'first_name': ft.TextField(label='name'),
            'last_name': ft.TextField(label='surname'),
            'is_staff': ft.Checkbox(label='is staff'),
            'is_superuser': ft.Checkbox(label='is superuser'),
            'is_active': ft.Checkbox(label='is active'),
            'email': ft.TextField(label='email', keyboard_type=ft.KeyboardType.EMAIL)
        }


class PermissionsCreateUpdateDialog(BaseCreateUpdateDialog):
    url = '/admin/permissions/'

    def get_fields(self):
        return {
            'name': ft.TextField(label='name'),
            'content_type': CustomDropDown(),
            'codename': ft.TextField(label='codename')
        }


class ContentTypesCreateUpdateDialog(BaseCreateUpdateDialog):
    url = '/admin/content_types/'

    def get_fields(self):
        return {
            'app_label': ft.TextField(label='app label'),
            'model': ft.TextField(label='model')
        }


class GroupsCreateUpdateDialog(BaseCreateUpdateDialog):
    url = '/admin/groups/'

    def get_fields(self):
        return {
            'name': ft.TextField(label='name')
        }


class DishesCreateUpdateDialog(BaseCreateUpdateDialog):
    url = '/food/dishes/'

    def get_fields(self):
        return {
            'name': ft.TextField(label='name'),
            'description': ft.TextField(label='description', multiline=True),
            'weight': ft.TextField(
                label='weight',
                keyboard_type=ft.KeyboardType.NUMBER,
                input_filter=NumbersOnlyInputFilter()
            ),
            'price': ft.TextField(
                label='weight',
                keyboard_type=ft.KeyboardType.NUMBER,
                input_filter=NumbersOnlyInputFilter()
            ),
            'image': ft.Image()
        }
