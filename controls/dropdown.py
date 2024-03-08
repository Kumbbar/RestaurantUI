import flet as ft

from core.data_models_list import ContentTypesDataModel
from data_models import BaseDataModel


class CustomDropDown(ft.UserControl):
    name: str
    data_model: BaseDataModel

    def __init__(self, label: str):
        super().__init__()
        self.value = None

        self.content = ft.Dropdown(
            width=600,
            label=label,
            on_change=self.change_option,
            value=self.value
        )

    def change_option(self, _):
        self.value = self.content.value
        self.update()

    def get_key_and_name(self, data):
        result = list()
        for row in data:
            result.append(
                dict(
                    key=getattr(row, 'id'),
                    text=getattr(row, self.__class__.name)
                )
            )
        return result

    def update(self):
        self.content.value = self.value
        super().update()

    def build(self):
        return self.content

    def did_mount(self):
        data = self.__class__.data_model(self.page)
        self.add_options(data.result_list)
        self.update()

    def add_options(self, data):
        key_name_data = self.get_key_and_name(data)
        for data in key_name_data:
            self.content.options.append(
                ft.dropdown.Option(**data)
            )


