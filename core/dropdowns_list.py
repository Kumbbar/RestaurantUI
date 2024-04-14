from controls.dropdown import CustomDropDown
from core.data_models_list import ContentTypesDataModel, DishTypesDataModel, UsersDataModel, RestaurantDataModel, \
    MenuDataModel, ClientsDataModel, TablesDataModel, DishesDataModel, MenuPlanDishesDataModel, \
    RestaurantTablesDataModel


class ContentTypeDropDown(CustomDropDown):
    name = 'model'
    data_model = ContentTypesDataModel


class DishTypeDropDown(CustomDropDown):
    name = 'name'
    data_model = DishTypesDataModel


class DishDropDown(CustomDropDown):
    name = 'name'
    data_model = DishesDataModel


class MenuPlanDishesDropDown(CustomDropDown):
    name = 'name'
    data_model = MenuPlanDishesDataModel


class UserDropDown(CustomDropDown):
    name = 'username'
    data_model = UsersDataModel


class RestaurantDropDown(CustomDropDown):
    name = 'name'
    data_model = RestaurantDataModel


class MenuDropDown(CustomDropDown):
    name = 'name'
    data_model = MenuDataModel


class ClientDropDown(CustomDropDown):
    name = 'surname'
    data_model = ClientsDataModel


class TablesDropDown(CustomDropDown):
    name = 'number'
    data_model = TablesDataModel


class RestaurantTablesDropDown(CustomDropDown):
    name = 'number'
    data_model = RestaurantTablesDataModel