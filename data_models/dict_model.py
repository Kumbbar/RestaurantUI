from data_models import BaseDataModel


class DictDataModeL(BaseDataModel):
    name: str

    def __init__(self, page):
        super().__init__(page)
        self.foreign_data = self.get_key_value()

    def get_key_value(self):
        result = dict()
        for row in self.result_list:
            result[getattr(row, 'id')] = getattr(row, self.__class__.name)
        return result