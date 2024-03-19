from controls.datatables import (ManySelectionsMixinDatatable, BaseDatatable, SearchMixinDatatable,
                                 ExcludeIdsMixinDatatable)
from core.data_models_list import PermissionsDataModel, UserPermissionsDataModel


class PermissionsManySelectionsTable(ManySelectionsMixinDatatable, ExcludeIdsMixinDatatable,
                                     SearchMixinDatatable, BaseDatatable):
    visible_columns = ['id', 'codename']
    data_model = PermissionsDataModel

    def get_params_for_request(self):
        result = super().get_params_for_request()
        result['page_size'] = 100000
        return result


class UserPermissionsManySelectionsTable(ManySelectionsMixinDatatable, SearchMixinDatatable, BaseDatatable):
    visible_columns = ['id', 'codename']
    data_model = UserPermissionsDataModel

