from controls.items import NavigationTile
import flet_core as ft

from core.datatables_list import UsersTable, PermissionsTable, ContentTypesTable, GroupsTypesTable, DishesTable, \
    DishTypesTable

PASS = ft.Container(
            width=300,
            bgcolor='yellow'
)


def create_tiles_scroll(tiles):
    return ft.Row(
        height=430,
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
            next_control=PASS
        ),

    ]
    return [create_tiles_scroll(admin_tiles)]


def get_menu_tiles():
    menu_tiles = [
        NavigationTile(
            'MENU',
            ft.icons.MENU_BOOK,
            next_control=PASS
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
        )
    ]
    return menu_tiles
