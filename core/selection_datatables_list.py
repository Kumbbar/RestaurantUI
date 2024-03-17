from controls.datatables import ManySelectionsDatatable
from core.data_models_list import PermissionsDataModel


class PermissionsManySelectionsTable(ManySelectionsDatatable):
    visible_columns = ['id', 'codename']
    data_model = PermissionsDataModel
