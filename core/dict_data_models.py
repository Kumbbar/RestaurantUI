from core.data_models_list import ContentTypesDataModel, DishTypesDataModel, UsersDataModel
from data_models.dict_model import DictDataModeL


class ContentTypeDictDataModeL(DictDataModeL, ContentTypesDataModel):
    name = 'model'


class DishTypeDictDataModeL(DictDataModeL, DishTypesDataModel):
    name = 'name'
