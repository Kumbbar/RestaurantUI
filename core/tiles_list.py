from controls.items import NavigationTile
import flet_core as ft

from core.datatables_list import UsersTable, PermissionsTable, ContentTypesTable

PASS = ft.Container(
            height=400,
            width=300,
            bgcolor='yellow'
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
        )
    ]
    return admin_tiles
