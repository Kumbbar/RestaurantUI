import flet as ft

from core.data_models_list import ContentTypesDataModel
from data_models import BaseDataModel


class CustomDropDown(ft.UserControl):
    name: str
    data_model: BaseDataModel

    def __init__(self, label: str, width=600):
        super().__init__()
        self.value = None

        self.dropdown = ft.Dropdown(
            width=width,
            label=label,
            on_change=self.change_option,
            value=self.value,
            col=8
        )
        self.search_field = ft.TextField(label='dropdown search', width=100, on_change=self.search_field_change, col=4)
        self.content = ft.ResponsiveRow(
            controls=[self.dropdown, self.search_field]
        )

    def search_field_change(self, _):
        self.dropdown.options.clear()
        self.get_data()

    def change_option(self, _):
        if self.dropdown.value == 'None':  # For some strange empty option logic
            self.value = ''
        else:
            self.value = self.dropdown.value
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
        self.dropdown.value = self.value
        super().update()

    def build(self):
        return self.content

    def did_mount(self):
        self.get_data()

    def get_data(self):
        request_data = dict(params=dict(search=self.search_field.value))
        data = self.__class__.data_model(self.page, **request_data)
        if data.result_list:
            self.add_options(data.result_list)
        self.update()

    def add_options(self, data):
        key_name_data = self.get_key_and_name(data)
        self.dropdown.options.append(
            ft.dropdown.Option(key='None')
        )
        for data in key_name_data:
            self.dropdown.options.append(
                ft.dropdown.Option(**data),

            )


class OrderStageDropDown(CustomDropDown):
    def get_data(self):
        data = [
            dict(
                key='not ready',
                text='not ready'
            ),
            dict(
                key='ready',
                text='ready'
            ),
            dict(
                key='finished',
                text='finished'
            )
        ]
        self.dropdown.options.append(
            ft.dropdown.Option(key='None')
        )
        for obj in data:
            self.dropdown.options.append(
                ft.dropdown.Option(**obj),

            )
        self.update()
