import copy

from controls.dish_report import DishReport
from controls.items import NavigationTile, CustomWidthNavigationTile
import flet_core as ft

from controls.many_to_many import ManyToManyDataControl
from controls.settings import SettingsContainer
from core.datatables_list import UsersTable, PermissionsTable, ContentTypesTable, GroupsTypesTable, DishesTable, \
    DishTypesTable, RestaurantTable, MenuTable, RestaurantPlanMenuTable, ClientsTable, TablesTable, \
    OrdersTable, TableReservationTable, ClientsBlackListTable
from core.many_to_many_list import UserPermissionsManyToManyDataControl
from core.order_dishes_table import OrderDishesCookTable, OrderDishesReadyTable
from core.selection_datatables_list import UserGroupsManySelectionsTable

PASS = ft.Container(
            width=300,
            height=200,
            bgcolor='yellow'
)


def create_tiles_scroll(tiles):
    return ft.Row(
        height=320,
        controls=tiles,
        wrap=True,
        spacing=5,
        run_spacing=10,
        alignment=ft.MainAxisAlignment.CENTER,
        scroll=ft.ScrollMode.ALWAYS
    )


def get_admin_tiles():
    admin_tiles = [
        CustomWidthNavigationTile(
            'USERS',
            ft.icons.PERSON,
            next_control=UsersTable(),
            width=200
        ),
        NavigationTile(
                'PERMISSIONS',
                ft.icons.RULE,
                next_control=PermissionsTable()
        ),
        NavigationTile(
            'CONTENT TYPES',
            ft.icons.DATASET,
            next_control=ContentTypesTable()
        ),
        NavigationTile(
                    'GROUPS',
                    ft.icons.GROUP,
                    next_control=GroupsTypesTable()
        )

    ]
    return [create_tiles_scroll(admin_tiles)]


def get_menu_tiles():
    menu_tiles = [
        NavigationTile(
            'RESTAURANTS',
            ft.icons.RESTAURANT,
            next_control=RestaurantTable(),
        ),
        CustomWidthNavigationTile(
            width=200,
            title='MENU',
            icon=ft.icons.MENU_BOOK,
            next_control=MenuTable()
        ),
        NavigationTile(
            'DISHES',
            ft.icons.EMOJI_FOOD_BEVERAGE,
            next_control=DishesTable()
        ),
        NavigationTile(
            'DISH TYPES',
            ft.icons.EMOJI_FOOD_BEVERAGE_OUTLINED,
            next_control=DishTypesTable()
        ),
        NavigationTile(
            'RESTAURANT TABLES',
            ft.icons.TABLE_RESTAURANT_ROUNDED,
            next_control=TablesTable()
        ),
        NavigationTile(
            'PLAN MENU',
            ft.icons.ACCESS_TIME,
            next_control=RestaurantPlanMenuTable()
        ),
        NavigationTile(
            'RESTAURANT REPORT',
            ft.icons.DOCUMENT_SCANNER,
            next_control=DishReport()
        )
    ]
    return [create_tiles_scroll(menu_tiles)]


def get_clients_service_tiles():
    menu_tiles = [
        NavigationTile(
            'TABLE RESERVATION',
            ft.icons.TABLE_RESTAURANT,
            next_control=TableReservationTable(),
        ),
        CustomWidthNavigationTile(
            width=200,
            title='READY DISHES',
            icon=ft.icons.EMOJI_FOOD_BEVERAGE,
            next_control=OrderDishesReadyTable()
        ),
        CustomWidthNavigationTile(
            width=200,
            title='ORDER',
            icon=ft.icons.ATTACH_MONEY,
            next_control=OrdersTable()
        ),
        NavigationTile(
            'BLACK LIST',
            ft.icons.PERSON_OFF,
            next_control=ClientsBlackListTable()
        ),
        NavigationTile(
            'CLIENTS',
            ft.icons.PERSON,
            next_control=ClientsTable()
        )
    ]
    return [create_tiles_scroll(menu_tiles)]


def get_cooking_tiles():
    menu_tiles = [
        NavigationTile(
            'ORDERED DISHES',
            ft.icons.EMOJI_FOOD_BEVERAGE,
            next_control=OrderDishesCookTable(),
        )
    ]
    return [create_tiles_scroll(menu_tiles)]


def get_settings():
    settings = [
        SettingsContainer()
    ]
    return [create_tiles_scroll(settings)]
