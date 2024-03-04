from controls.datatables import PydanticDatatable
from core.data_models_list import PermissionsDataModel, UsersDataModel, ContentTypesDataModel, GroupsDataModel, \
    DishesDataModel
from core.dialogs_list import PermissionsCreateUpdateDialog, UsersCreateUpdateDialog, ContentTypesCreateUpdateDialog, \
    GroupsCreateUpdateDialog, DishesCreateUpdateDialog


# ADMIN

class UsersTable(PydanticDatatable):
    visible_columns = ['id', 'username', 'first_name', 'last_name', 'is_staff', 'email']
    url = '/admin/users/'
    dialog = UsersCreateUpdateDialog
    data_model = UsersDataModel


class PermissionsTable(PydanticDatatable):
    visible_columns = ['id', 'content_type', 'codename']
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

class DishesTable(PydanticDatatable):
    visible_columns = [
        'name',
        'dish_type',
        'price',
        'image'
    ]
    url = '/food/dishes/'
    dialog = DishesCreateUpdateDialog
    data_model = DishesDataModel
