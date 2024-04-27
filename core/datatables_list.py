from controls.datatables import PydanticDatatable, ImageMixinDatatable, SearchMixinDatatable, BaseDatatable
from controls.dropdown import OrderStageDropDown
from core.data_models_list import PermissionsDataModel, UsersDataModel, ContentTypesDataModel, GroupsDataModel, \
    DishesDataModel, DishTypesDataModel, RestaurantDataModel, MenuDataModel, RestaurantPlanMenuDataModel, \
    ClientsDataModel, TablesDataModel, OrdersDataModel, OrderDishesDataModel, OrderDishesCookDataModel, \
    TableReservationDataModel, ClientsBlackListDataModel
from core.dialogs_list import (PermissionsCreateUpdateDialog, UsersCreateUpdateDialog, ContentTypesCreateUpdateDialog, \
                               GroupsCreateUpdateDialog, DishesCreateUpdateDialog, DishTypesCreateUpdateDialog,
                               RestaurantCreateUpdateDialog, \
                               MenuCreateUpdateDialog, RestaurantPlanMenuCreateUpdateDialog, ClientsCreateUpdateDialog,
                               TablesCreateUpdateDialog,
                               OrdersCreateUpdateDialog, TableReservationCreateUpdateDialog,
                               ClientsBlackListCreateUpdateDialog)
from core.dict_data_models import ContentTypeDictDataModeL, DishTypeDictDataModeL, MenuDictDataModeL, \
    RestaurantDictDataModeL, ClientDictDataModel, TablesDictDataModel, DishDictDataModel, RestaurantTablesDictDataModel
from core.dropdowns_list import RestaurantDropDown
from pydantic_models.restaurant_plan_menu import RestaurantPlanMenuResponse
from services.requests import RequestMethod


import flet_core as ft

# ADMIN

class UsersTable(PydanticDatatable):
    visible_columns = ['id', 'username', 'first_name', 'last_name', 'is_staff', 'email']
    url = '/admin/users/'
    dialog = UsersCreateUpdateDialog
    data_model = UsersDataModel


class PermissionsTable(PydanticDatatable):
    visible_columns = ['id', 'content_type', 'codename']
    foreign_data_template = {
        'content_type': ContentTypeDictDataModeL
    }
    dialog = PermissionsCreateUpdateDialog
    url = '/admin/permissions/'
    data_model = PermissionsDataModel


class ContentTypesTable(PydanticDatatable):
    visible_columns = ['id', 'app_label', 'model']
    url = '/admin/content_types/'
    dialog = ContentTypesCreateUpdateDialog
    data_model = ContentTypesDataModel


class GroupsTypesTable(PydanticDatatable):
    visible_columns = ['id', 'name']
    url = '/admin/groups/'
    dialog = GroupsCreateUpdateDialog
    data_model = GroupsDataModel


# FOOD

class DishesTable(ImageMixinDatatable, PydanticDatatable):
    visible_columns = [
        'id',
        'name',
        'dish_type',
        'price',
        'description',
        'image'
    ]
    url = '/food/dishes/'
    foreign_data_template = {
        'dish_type': DishTypeDictDataModeL
    }
    dialog = DishesCreateUpdateDialog
    data_model = DishesDataModel


class MenuTable(PydanticDatatable):
    visible_columns = [
        'id',
        'name'
    ]
    url = '/food/menu/'
    dialog = MenuCreateUpdateDialog
    data_model = MenuDataModel


class DishTypesTable(PydanticDatatable):
    visible_columns = [
        'id',
        'name'
    ]
    url = '/food/dish_types/'
    dialog = DishTypesCreateUpdateDialog
    data_model = DishTypesDataModel


class RestaurantTable(PydanticDatatable):
    visible_columns = [
        'id',
        'name'
    ]
    url = '/food/restaurants/'
    dialog = RestaurantCreateUpdateDialog
    data_model = RestaurantDataModel


class RestaurantPlanMenuTable(PydanticDatatable):
    visible_columns = [
        'id',
        'restaurant',
        'menu',
        'date_start',
        'date_end',
    ]
    url = '/food/restaurant_plan_menu/'

    foreign_data_template = {
        'menu': MenuDictDataModeL,
        'restaurant': RestaurantDictDataModeL,
    }
    search_dropdowns = {
        'restaurant': RestaurantDropDown('restaurant', width=200)
    }
    dialog = RestaurantPlanMenuCreateUpdateDialog
    data_model = RestaurantPlanMenuDataModel


class ClientsTable(PydanticDatatable):
    visible_columns = ['id', 'name', 'surname', 'phone_number']
    url = '/food/clients/'
    dialog = ClientsCreateUpdateDialog
    data_model = ClientsDataModel


class ClientsBlackListTable(PydanticDatatable):
    visible_columns = ['id', 'client']
    url = '/food/clients_black_list/'
    dialog = ClientsBlackListCreateUpdateDialog
    data_model = ClientsBlackListDataModel
    foreign_data_template = {
        'client': ClientDictDataModel
    }


class TablesTable(PydanticDatatable):
    visible_columns = ['id', 'number', 'restaurant', 'description', ]
    url = '/food/tables/'
    foreign_data_template = {
        'restaurant': RestaurantDictDataModeL
    }
    dialog = TablesCreateUpdateDialog
    data_model = TablesDataModel


class OrdersTable(PydanticDatatable):
    visible_columns = ['id', 'client', 'table', 'stage', 'created_at']
    url = '/food/orders/'
    foreign_data_template = {
        'client': ClientDictDataModel,
        'table': RestaurantTablesDictDataModel,
    }
    dialog = OrdersCreateUpdateDialog
    data_model = OrdersDataModel

    search_dropdowns = {
        'stage': OrderStageDropDown('stage', width=200)
    }


class TableReservationTable(PydanticDatatable):
    visible_columns = [
        'id',
        'table',
        'client',
        'time_of_start',
        'time_of_end',
        'confirmed',
        'has_come'
    ]
    url = '/food/table_reservation/'
    foreign_data_template = {
        'client': ClientDictDataModel,
        'table': RestaurantTablesDictDataModel,
    }
    dialog = TableReservationCreateUpdateDialog
    data_model = TableReservationDataModel
