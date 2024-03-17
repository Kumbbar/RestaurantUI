from flet_core import NumbersOnlyInputFilter

from controls.datepickers import InputDatePicker
from controls.dialogs import BaseCreateUpdateDialog
import flet_core as ft

from controls.file_pickers import FilePickerImage

from core.dropdowns_list import ContentTypeDropDown, DishTypeDropDown, UserDropDown


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
            'email': ft.TextField(label='email', keyboard_type=ft.KeyboardType.EMAIL),
        }


class PermissionsCreateUpdateDialog(BaseCreateUpdateDialog):
    url = '/admin/permissions/'

    def get_fields(self):
        return {
            'name': ft.TextField(label='name'),
            'content_type': ContentTypeDropDown('content type'),
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
            'weight': ft.TextField(
                label='weight',
                keyboard_type=ft.KeyboardType.NUMBER,
                input_filter=NumbersOnlyInputFilter()
            ),
            'dish_type': DishTypeDropDown('dish type'),
            'price': ft.TextField(
                label='price',
                keyboard_type=ft.KeyboardType.NUMBER,
                input_filter=NumbersOnlyInputFilter()
            ),
            'image': FilePickerImage(),
            'description': ft.TextField(label='description', multiline=True),
        }


class DishTypesCreateUpdateDialog(BaseCreateUpdateDialog):
    url = '/food/dish_types/'

    def get_fields(self):
        return {
            'name': ft.TextField(label='name')
        }


class RestaurantCreateUpdateDialog(BaseCreateUpdateDialog):
    url = '/food/restaurants/'

    def get_fields(self):
        return {
            'name': ft.TextField(label='name'),
            'boss': UserDropDown('boss'),
            'latitude': ft.TextField(label='latitude', keyboard_type=ft.KeyboardType.NUMBER),
            'longitude': ft.TextField(label='longitude', keyboard_type=ft.KeyboardType.NUMBER),
            'date_of_open': InputDatePicker('date of open')
        }
