from controls.datatables import PydanticDatatable
from pydantic_models.users import User, UserResponse
from pydantic_models.permissions import Permission, PermissionResponse
from pydantic_models.content_types import ContentType, ContentTypeResponse


class UsersTable(PydanticDatatable):
    url = '/admin/users/'
    table_pydantic_model = User
    table_response_model = UserResponse


class PermissionsTable(PydanticDatatable):
    url = '/admin/permissions/'
    table_pydantic_model = Permission
    table_response_model = PermissionResponse


class ContentTypesTable(PydanticDatatable):
    url = '/admin/content_types/'
    table_pydantic_model = ContentType
    table_response_model = ContentTypeResponse
