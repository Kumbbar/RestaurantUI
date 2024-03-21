from controls.datatables import PydanticDatatable, ImageMixinDatatable
from core.data_models_list import PermissionsDataModel, UsersDataModel, ContentTypesDataModel, GroupsDataModel, \
    DishesDataModel, DishTypesDataModel, RestaurantDataModel, MenuDataModel
from core.dialogs_list import PermissionsCreateUpdateDialog, UsersCreateUpdateDialog, ContentTypesCreateUpdateDialog, \
    GroupsCreateUpdateDialog, DishesCreateUpdateDialog, DishTypesCreateUpdateDialog, RestaurantCreateUpdateDialog, \
    MenuCreateUpdateDialog
from core.dict_data_models import ContentTypeDictDataModeL, DishTypeDictDataModeL


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
