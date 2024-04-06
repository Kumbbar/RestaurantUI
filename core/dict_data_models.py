from core.data_models_list import ContentTypesDataModel, DishTypesDataModel, UsersDataModel, MenuDataModel, \
    RestaurantDataModel
from data_models.dict_model import DictDataModeL


class ContentTypeDictDataModeL(DictDataModeL, ContentTypesDataModel):
    name = 'model'


class DishTypeDictDataModeL(DictDataModeL, DishTypesDataModel):
    name = 'name'


class MenuDictDataModeL(DictDataModeL, MenuDataModel):
    name = 'name'


class RestaurantDictDataModeL(DictDataModeL, RestaurantDataModel):
    name = 'name'
