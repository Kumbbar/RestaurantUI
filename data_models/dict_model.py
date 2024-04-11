from typing import Optional, List, Iterable, Union

from data_models import BaseDataModel


class DictDataModeL(BaseDataModel):
    name: Union[List[str], str]

    def __init__(self, page):
        super().__init__(page)
        self.foreign_data = self.get_key_value()

    def get_key_value(self):
        result = dict()
        for row in self.result_list:
            if isinstance(self.__class__.name, (tuple, list)):
                row_result = []
                for name in self.__class__.name:
                    row_result.append(getattr(row, name))
                row_foreign_data = ' '.join(row_result)
            else:
                row_foreign_data = getattr(row, self.__class__.name)
            result[getattr(row, 'id')] = row_foreign_data
        return result