from controls.datatables import SearchMixinDatatable, BaseDatatable, PydanticDatatable
from core.data_models_list import OrderDishesDataModel, OrderDishesCookDataModel, OrderDishesReadyDataModel
from core.dict_data_models import DishDictDataModel, TablesDictDataModel, RestaurantTablesDictDataModel, \
    MenuPlanDishesDictDataModel
from services.requests import RequestMethod

import flet_core as ft


class OrderDishesTable(PydanticDatatable):
    visible_columns = ['id', 'dish', 'count', 'stage']
    data_model = OrderDishesDataModel
    foreign_data_template = {
        'dish': MenuPlanDishesDictDataModel,
    }
    url = '/food/order_dishes/'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.header_navigation[0]  # delete create button

    def show_create_dialog(self, _):
        """delete create logic"""
        pass

    def obj_event(self, e):
        """delete row click logic"""
        pass

    def show_delete_dialog(self, e):
        """delete without dialog"""
        response = self.page.current_view.auth_service.send_closed_request(
            RequestMethod.DELETE,
            f'{self.__class__.url}{self.extra_url}/',
            json=dict(order_dish_id=e.control.data)
        )
        if response.ok:
            self.refresh_data()


class OrderDishesCookTable(OrderDishesTable):
    visible_columns = ['id', 'dish', 'count', 'table', 'created_at']
    url = '/food/order_dishes_cook/'
    foreign_data_template = {
        'dish': MenuPlanDishesDictDataModel,
        'table': RestaurantTablesDictDataModel
    }
    data_model = OrderDishesCookDataModel

    def order_dish_event(self, e):
        response = self.page.current_view.auth_service.send_closed_request(
            RequestMethod.PUT,
            f'{self.__class__.url}{e.control.data}/',
        )
        if response.ok:
            self.refresh_data()

    def show_delete_dialog(self, e):
        pass

    def add_row_end(self, data_row, row):
        data_row.cells.append(
            ft.DataCell(
                ft.IconButton(
                    ft.icons.CHECK,
                    icon_color=ft.colors.GREEN_400,
                    data=row.id,
                    on_click=self.order_dish_event,
                )
            )
        )


class OrderDishesReadyTable(OrderDishesCookTable):
    url = '/food/order_dishes_ready/'
    data_model = OrderDishesReadyDataModel
