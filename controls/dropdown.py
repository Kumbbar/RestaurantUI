import flet as ft

from core.data_models_list import ContentTypesDataModel


class CustomDropDown(ft.UserControl):
    name: str = 'model'

    def __init__(self):
        super().__init__()
        self.value = None

        self.content = ft.Dropdown(
            width=600,
            on_change=self.change_option
        )

    def change_option(self, _):
        self.value = self.content.value

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

    def build(self):
        return self.content

    def did_mount(self):
        data = ContentTypesDataModel(self.page)
        self.add_options(data.result_list)
        self.update()

    def add_options(self, data):
        key_name_data = self.get_key_and_name(data)
        for data in key_name_data:
            self.content.options.append(
                ft.dropdown.Option(**data)
            )


