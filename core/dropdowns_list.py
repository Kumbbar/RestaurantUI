from controls.dropdown import CustomDropDown
from core.data_models_list import ContentTypesDataModel, DishTypesDataModel, UsersDataModel, RestaurantDataModel


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
