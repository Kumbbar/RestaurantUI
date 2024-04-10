import copy

from controls.items import NavigationTile, CustomWidthNavigationTile
import flet_core as ft

from controls.many_to_many import ManyToManyDataControl
from core.datatables_list import UsersTable, PermissionsTable, ContentTypesTable, GroupsTypesTable, DishesTable, \
    DishTypesTable, RestaurantTable, MenuTable, RestaurantPlanMenuTable, ClientsTable
from core.many_to_many_list import UserPermissionsManyToManyDataControl

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
        NavigationTile(
            'USERS',
            ft.icons.PERSON,
            next_control=UsersTable()
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
        ),
        NavigationTile(
            'CONTENT TYPES',
            ft.icons.DATASET,
            next_control=PASS
        ),
        NavigationTile(
            'CONTENT TYPES',
            ft.icons.DATASET,
            next_control=PASS
        ),
        NavigationTile(
            'CONTENT TYPES',
            ft.icons.DATASET,
            next_control=PASS
        ),
        NavigationTile(
            'CONTENT TYPES',
            ft.icons.DATASET,
            next_control=PASS
        ),
        NavigationTile(
            'CONTENT TYPES',
            ft.icons.DATASET,
            next_control=PASS
        ),
        NavigationTile(
            'CONTENT TYPES',
            ft.icons.DATASET,
            next_control=PASS
        ),
        NavigationTile(
            'CONTENT TYPES',
            ft.icons.DATASET,
            next_control=UserPermissionsManyToManyDataControl('PERMISSIONS')
        ),

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
            'PLAN MENU',
            ft.icons.ACCESS_TIME,
            next_control=RestaurantPlanMenuTable()
        ),
    ]
    return [create_tiles_scroll(menu_tiles)]


def get_clients_service_tiles():
    menu_tiles = [
        NavigationTile(
            'TABLE RESERVATION',
            ft.icons.TABLE_RESTAURANT,
            next_control=PASS,
        ),
        CustomWidthNavigationTile(
            width=200,
            title='ORDER',
            icon=ft.icons.ATTACH_MONEY,
            next_control=PASS
        ),
        NavigationTile(
            'BLACK LIST',
            ft.icons.PERSON_OFF,
            next_control=PASS
        ),
        NavigationTile(
            'CLIENTS',
            ft.icons.PERSON,
            next_control=ClientsTable()
        )
    ]
    return [create_tiles_scroll(menu_tiles)]