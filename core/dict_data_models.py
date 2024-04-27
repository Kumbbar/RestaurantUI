from core.data_models_list import ContentTypesDataModel, DishTypesDataModel, UsersDataModel, MenuDataModel, \
    RestaurantDataModel, ClientsDataModel, TablesDataModel, DishesDataModel, RestaurantTablesDataModel, \
    MenuPlanDishesDataModel
from data_models.dict_model import DictDataModeL


class ContentTypeDictDataModeL(DictDataModeL, ContentTypesDataModel):
    name = 'model'


class DishTypeDictDataModeL(DictDataModeL, DishTypesDataModel):
    name = 'name'


class MenuDictDataModeL(DictDataModeL, MenuDataModel):
    name = 'name'


class RestaurantDictDataModeL(DictDataModeL, RestaurantDataModel):
    name = 'name'


class ClientDictDataModel(DictDataModeL, ClientsDataModel):
    name = ['name', 'surname']


class TablesDictDataModel(DictDataModeL, TablesDataModel):
    name = 'number'


class RestaurantTablesDictDataModel(DictDataModeL, RestaurantTablesDataModel):
    name = 'number'


class DishDictDataModel(DictDataModeL, DishesDataModel):
    name = 'name'


class MenuPlanDishesDictDataModel(DictDataModeL, MenuPlanDishesDataModel):
    name = 'name'