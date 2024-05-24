import flet as ft

from consts.colors import PastelColors
from controls.bottom_sheets import BottomSheetOrderTotalPrice
from core.dropdowns_list import DishDropDown, MenuPlanDishesDropDown
from core.order_dishes_table import OrderDishesTable
from core.selection_datatables_list import PermissionsManySelectionsTable, BaseDatatable, \
    UserPermissionsManySelectionsTable
from services.requests import RequestMethod
from settings import BACKEND_BASE_URL


def get_param_ids(ids):
    return dict(
        ids=','.join(map(str, ids))
    )


class OrderDishEditor(ft.UserControl):
    def __init__(self, label_text):
        super().__init__()
        self.value = None
        self.current_order_dishes = OrderDishesTable(autoload=False)
        self.count_field = ft.TextField(label='count', value='1', col=6)
        self.add_button = ft.ElevatedButton(
                        'ADD',
                        bgcolor=PastelColors.LIGHT_BROWN,
                        color=ft.colors.WHITE,
                        on_click=self.add_button_click,
                        col=6,
                        height=50
                    )
        self.get_price_button = ft.ElevatedButton(
                        'GET ORDER TEMPLATE',
                        bgcolor=PastelColors.LIGHT_BROWN,
                        color=ft.colors.WHITE,
                        on_click=self.show_total_price_template,
                        col=12,
                        height=50
                    )
        self.dishes_dropdown = MenuPlanDishesDropDown('dish')

        self.content = ft.ResponsiveRow(
            controls=[
                ft.Text(label_text, col=12, weight=ft.FontWeight.BOLD, size=16),
                self.dishes_dropdown,
                self.count_field,
                self.add_button,
                ft.Column(
                    col=12,
                    controls=[
                        self.current_order_dishes,
                    ]
                ),
                self.get_price_button
            ]
        )

    def add_button_click(self, _):
        request_json = dict(
            count=self.count_field.value,
            dish_id=int(self.dishes_dropdown.value)
        )
        response = self.page.current_view.auth_service.send_closed_request(
            RequestMethod.POST,
            f'/food/order_dishes/{self.value}/',
            json=request_json
        )
        if response.ok:
            self.current_order_dishes.refresh_data()

    def build(self):
        return self.content

    def show_total_price_template(self, _):
        self.page.launch_url(f'{BACKEND_BASE_URL}/food/order_price_template/{self.value}')

    def update(self):
        self.current_order_dishes.extra_url = self.value
        self.current_order_dishes.refresh_data()
        super().update()

