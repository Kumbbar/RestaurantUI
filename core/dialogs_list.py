from flet_core import NumbersOnlyInputFilter

from controls.datepickers import InputDatePicker
from controls.dialogs import BaseCreateUpdateDialog
import flet_core as ft

from controls.file_pickers import FilePickerImage
from controls.menu_render import CreateMenuTemplate
from controls.order_dishes import OrderDishEditor

from core.dropdowns_list import ContentTypeDropDown, DishTypeDropDown, UserDropDown, RestaurantDropDown, MenuDropDown, \
    ClientDropDown, TablesDropDown, RestaurantTablesDropDown
from core.many_to_many_list import UserPermissionsManyToManyDataControl, UserGroupsManyToManyDataControl, \
    GroupPermissionsManyToManyDataControl, MenuDishesManyToManyDataControl


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
            'current_restaurant': RestaurantDropDown(' current restaurant'),
            'password': ft.TextField(label='password', keyboard_type=ft.KeyboardType.VISIBLE_PASSWORD)
        }

    def get_extra_controls(self):
        return {
            'permissions': UserPermissionsManyToManyDataControl('PERMISSIONS'),
            'groups': UserGroupsManyToManyDataControl('GROUPS'),
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

    def get_extra_controls(self):
        return {
            'permissions': GroupPermissionsManyToManyDataControl('PERMISSIONS'),
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


class MenuCreateUpdateDialog(BaseCreateUpdateDialog):
    url = '/food/menu/'

    def get_fields(self):
        return {
            'name': ft.TextField(label='name')
        }

    def get_extra_controls(self):
        return {
            'dishes': MenuDishesManyToManyDataControl('DISHES'),
            'dish_ordering': CreateMenuTemplate()
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


class RestaurantPlanMenuCreateUpdateDialog(BaseCreateUpdateDialog):
    url = '/food/restaurant_plan_menu/'

    def get_fields(self):
        return {
            'restaurant': RestaurantDropDown('restaurant'),
            'menu': MenuDropDown('menu'),
            'date_start': InputDatePicker('date start'),
            'date_end': InputDatePicker('date end')
        }


class ClientsCreateUpdateDialog(BaseCreateUpdateDialog):
    url = '/food/clients/'

    def get_fields(self):
        return {
            'name': ft.TextField(label='name'),
            'surname': ft.TextField(label='surname'),
            'patronymic': ft.TextField(label='patronymic'),
            'phone_number': ft.TextField(label='codename', value='+')
        }


class TablesCreateUpdateDialog(BaseCreateUpdateDialog):
    url = '/food/tables/'

    def get_fields(self):
        return {
            'number': ft.TextField(label='number'),
            'restaurant': RestaurantDropDown('restaurant'),
            'description': ft.TextField(label='description')
        }


class OrdersCreateUpdateDialog(BaseCreateUpdateDialog):
    url = '/food/orders/'

    def get_fields(self):
        return {
            'client': ClientDropDown('client'),
            'table': RestaurantTablesDropDown('table number')
        }

    def get_extra_controls(self):
        return {
            'order_dishes': OrderDishEditor('ORDER DISHES')
        }
