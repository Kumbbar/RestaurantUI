from controls.datatables import (ManySelectionsMixinDatatable, BaseDatatable, SearchMixinDatatable,
                                 ExcludeIdsMixinDatatable, ImageMixinDatatable)
from core.data_models_list import (PermissionsDataModel, UserPermissionsDataModel, UserGroupsDataModel,
                                   GroupsDataModel, GroupPermissionsDataModel, DishesDataModel, MenuDishesDataModel
                                   )


class PermissionsManySelectionsTable(ManySelectionsMixinDatatable, ExcludeIdsMixinDatatable,
                                     SearchMixinDatatable, BaseDatatable):
    visible_columns = ['id', 'codename']
    data_model = PermissionsDataModel


class UserPermissionsManySelectionsTable(ManySelectionsMixinDatatable, SearchMixinDatatable, BaseDatatable):
    visible_columns = ['id', 'codename']
    data_model = UserPermissionsDataModel


class GroupsManySelectionsTable(ManySelectionsMixinDatatable, ExcludeIdsMixinDatatable,
                                SearchMixinDatatable, BaseDatatable):
    visible_columns = ['id', 'name']
    data_model = GroupsDataModel


class UserGroupsManySelectionsTable(ManySelectionsMixinDatatable, SearchMixinDatatable, BaseDatatable):
    visible_columns = ['id', 'name']
    data_model = UserGroupsDataModel


class GroupPermissionsManySelectionsTable(ManySelectionsMixinDatatable, SearchMixinDatatable, BaseDatatable):
    visible_columns = ['id', 'codename']
    data_model = GroupPermissionsDataModel


class DishesManySelectionsTable(ImageMixinDatatable, ManySelectionsMixinDatatable, ExcludeIdsMixinDatatable,
                                SearchMixinDatatable, BaseDatatable):
    visible_columns = ['id', 'name', 'image']
    data_model = DishesDataModel


class MenuDishesManySelectionsTable(ImageMixinDatatable, ManySelectionsMixinDatatable,
                                    SearchMixinDatatable, BaseDatatable):
    visible_columns = ['id', 'name', 'image']
    data_model = MenuDishesDataModel
