import math

import flet_core as ft

from consts.colors import PastelColors
from controls.bottom_sheets import BottomSheetDefaultWorkspace
from controls.pickers import InputDatePicker
from core.dropdowns_list import RestaurantDropDown
from services.requests import RequestMethod
from settings import DEFAULT_WORKSPACE_KEY, BACKEND_BASE_URL


class DishReport(ft.Container):
    def __init__(self):
        super().__init__()
        self.border_radius = 10
        self.padding = ft.Padding(10, 10, 10, 20)
        self.bgcolor = ft.colors.AMBER_50
        self.alignment = ft.alignment.center
        self.restaurant = RestaurantDropDown('restaurant')
        self.date_start = InputDatePicker('date start')
        self.date_end = InputDatePicker('date end')
        self.get_button = ft.ElevatedButton(
            text='GET',
            on_click=self.get_click,
            width=300,
            bgcolor=PastelColors.LIGHT_BROWN
        )
        self.content = ft.Column(
            [
                self.restaurant,
                self.date_start,
                self.date_end,
                self.get_button
            ]
        )
        self.bgcolor = PastelColors.SEA_GREEN

    def get_click(self, _):
        self.page.launch_url(
            f'{BACKEND_BASE_URL}/food/restaurant_report/?restaurant_id={self.restaurant.value}&time_of_start={self.date_start.value}&time_of_end={self.date_end.value}'
        )
