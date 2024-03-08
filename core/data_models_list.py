from data_models import BaseDataModel
from pydantic_models.content_types import ContentTypeResponse
from pydantic_models.dish_types import DishTypeResponse
from pydantic_models.dishes import DishResponse
from pydantic_models.groups import GroupResponse
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


class GroupsDataModel(BaseDataModel):
    url = '/admin/groups/'
    pydantic_model = GroupResponse


class DishesDataModel(BaseDataModel):
    url = '/food/dishes/'
    pydantic_model = DishResponse


class DishTypesDataModel(BaseDataModel):
    url = '/food/dish_types/'
    pydantic_model = DishTypeResponse
