from data_models import BaseDataModel
from pydantic_models.clients import ClientResponse
from pydantic_models.content_types import ContentTypeResponse
from pydantic_models.dish_types import DishTypeResponse
from pydantic_models.dishes import DishResponse
from pydantic_models.groups import GroupResponse
from pydantic_models.menu import MenuResponse
from pydantic_models.order import OrderResponse
from pydantic_models.order_dish import OrderDishResponse
from pydantic_models.order_dishes_cook import OrderDishCookResponse
from pydantic_models.permissions import PermissionResponse
from pydantic_models.restaurant_plan_menu import RestaurantPlanMenuResponse
from pydantic_models.restaurants import RestaurantResponse
from pydantic_models.table_reservation import TableReservationResponse
from pydantic_models.tables import TableResponse
from pydantic_models.user_profile import UserProfileResponse
from pydantic_models.users import UserResponse


class PermissionsDataModel(BaseDataModel):
    url = '/admin/permissions/'
    pydantic_model = PermissionResponse


class UserPermissionsDataModel(BaseDataModel):
    url = '/admin/user_permissions/'
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


class UserGroupsDataModel(BaseDataModel):
    url = '/admin/user_groups/'
    pydantic_model = GroupResponse


class GroupPermissionsDataModel(BaseDataModel):
    url = '/admin/group_permissions/'
    pydantic_model = PermissionResponse


class DishesDataModel(BaseDataModel):
    url = '/food/dishes/'
    pydantic_model = DishResponse


class MenuPlanDishesDataModel(BaseDataModel):
    url = '/food/planned_dishes/'
    pydantic_model = DishResponse


class MenuDataModel(BaseDataModel):
    url = '/food/menu/'
    pydantic_model = MenuResponse


class MenuDishesDataModel(BaseDataModel):
    url = '/food/menu_dishes/'
    pydantic_model = DishResponse


class DishTypesDataModel(BaseDataModel):
    url = '/food/dish_types/'
    pydantic_model = DishTypeResponse


class UserProfileDataModel(BaseDataModel):
    url = '/auth/me/'
    pydantic_model = UserProfileResponse


class RestaurantDataModel(BaseDataModel):
    url = '/food/restaurants/'
    pydantic_model = RestaurantResponse


class RestaurantPlanMenuDataModel(BaseDataModel):
    url = '/food/restaurant_plan_menu/'
    pydantic_model = RestaurantPlanMenuResponse


class ClientsDataModel(BaseDataModel):
    url = '/food/clients/'
    pydantic_model = ClientResponse


class TablesDataModel(BaseDataModel):
    url = '/food/tables/'
    pydantic_model = TableResponse


class RestaurantTablesDataModel(BaseDataModel):
    url = '/food/restaurant_tables/'
    pydantic_model = TableResponse


class TableReservationDataModel(BaseDataModel):
    url = '/food/table_reservation/'
    pydantic_model = TableReservationResponse


class OrdersDataModel(BaseDataModel):
    url = '/food/orders/'
    pydantic_model = OrderResponse


class OrderDishesDataModel(BaseDataModel):
    url = '/food/order_dishes/'
    pydantic_model = OrderDishResponse


class OrderDishesCookDataModel(BaseDataModel):
    url = '/food/order_dishes_cook/'
    pydantic_model = OrderDishCookResponse


class OrderDishesReadyDataModel(BaseDataModel):
    url = '/food/order_dishes_ready/'
    pydantic_model = OrderDishCookResponse  # same for cook
