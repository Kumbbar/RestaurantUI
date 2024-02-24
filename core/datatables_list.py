from controls.datatables import PydanticDatatable
from core.data_models_list import PermissionsDataModel, UsersDataModel, ContentTypesDataModel


class UsersTable(PydanticDatatable):
    visible_columns = ['id', 'username', 'first_name', 'last_name', 'is_staff', 'email']
    url = '/admin/users/'
    data_model = UsersDataModel


class PermissionsTable(PydanticDatatable):
    visible_columns = ['id', 'content_type', 'codename']
    url = '/admin/permissions/'
    data_model = PermissionsDataModel


class ContentTypesTable(PydanticDatatable):
    visible_columns = ['id', 'app_label', 'model']
    url = '/admin/content_types/'
    data_model = ContentTypesDataModel
