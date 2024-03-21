from controls.many_to_many import ManyToManyDataControl
from core.selection_datatables_list import UserPermissionsManySelectionsTable, PermissionsManySelectionsTable, \
    UserGroupsManySelectionsTable, GroupsManySelectionsTable, GroupPermissionsManySelectionsTable


class UserPermissionsManyToManyDataControl(ManyToManyDataControl):
    current_data_table = UserPermissionsManySelectionsTable
    all_data_table = PermissionsManySelectionsTable
    url = '/admin/user_permissions/'


class UserGroupsManyToManyDataControl(ManyToManyDataControl):
    current_data_table = UserGroupsManySelectionsTable
    all_data_table = GroupsManySelectionsTable
    url = '/admin/user_groups/'


class GroupPermissionsManyToManyDataControl(ManyToManyDataControl):
    current_data_table = GroupPermissionsManySelectionsTable
    all_data_table = PermissionsManySelectionsTable
    url = '/admin/group_permissions/'
