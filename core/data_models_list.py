from data_models import BaseDataModel
from pydantic_models.content_types import ContentTypeResponse
from pydantic_models.permissions import PermissionResponse
from pydantic_models.users import UserResponse


class PermissionsDataModel(BaseDataModel):
    url = '/admin/permissions/'
    pydantic_model = PermissionResponse


class UsersDataModel(BaseDataModel):
    url = '/admin/users/'
    pydantic_model = UserResponse


class ContentTypesDataModel(BaseDataModel):
    url = '/admin/content_types/'
    pydantic_model = ContentTypeResponse

