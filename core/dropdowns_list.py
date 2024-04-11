from controls.dropdown import CustomDropDown
from core.data_models_list import ContentTypesDataModel, DishTypesDataModel, UsersDataModel, RestaurantDataModel, \
    MenuDataModel, ClientsDataModel, OrderStagesDataModel, TablesDataModel


class ContentTypeDropDown(CustomDropDown):
    name = 'model'
    data_model = ContentTypesDataModel


class DishTypeDropDown(CustomDropDown):
    name = 'name'
    data_model = DishTypesDataModel


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


class OrderStageDropDown(CustomDropDown):
    name = 'name'
    data_model = OrderStagesDataModel


class TablesDropDown(CustomDropDown):
    name = 'number'
    data_model = TablesDataModel
