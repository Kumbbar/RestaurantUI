from controls.datatables import PydanticDatatable
from core.data_models_list import PermissionsDataModel, UsersDataModel, ContentTypesDataModel


class UsersTable(PydanticDatatable):
    visible_columns = ['id', 'username', 'first_name', 'last_name', 'is_staff', 'email']
    data_model = UsersDataModel


class PermissionsTable(PydanticDatatable):
    visible_columns = ['id', 'content_type', 'codename']
    data_model = PermissionsDataModel


class ContentTypesTable(PydanticDatatable):
    visible_columns = ['id', 'app_label', 'model']
    data_model = ContentTypesDataModel
