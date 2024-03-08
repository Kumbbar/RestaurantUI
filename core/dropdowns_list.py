from controls.dropdown import CustomDropDown
from core.data_models_list import ContentTypesDataModel, DishTypesDataModel


class ContentTypeDropDown(CustomDropDown):
    name = 'model'
    data_model = ContentTypesDataModel


class DishTypeDropDown(CustomDropDown):
    name = 'name'
    data_model = DishTypesDataModel
