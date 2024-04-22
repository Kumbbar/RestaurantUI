import flet_core as ft

from consts.colors import PastelColors
from controls.dialogs import LogoutDialog
from core.tiles_list import get_admin_tiles, get_menu_tiles, get_clients_service_tiles, get_cooking_tiles, get_settings
from settings import LOGIN_PAGE_VIEW_URL


class PermissionNavigationRailDestination(ft.NavigationRailDestination):
    def __init__(self, permission, workspace_data, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.permission = permission
        self.workspace_data = workspace_data


class MainMenu(ft.Container):
    def __init__(self):
        super().__init__()
        self.col = {
                "xs": 12,
                "sm": 3.8,
                "md": 3,
                "xl": 3
        }
        self.border_radius = 10

        self.destinations = [
            PermissionNavigationRailDestination(
                label='ADMIN',
                selected_icon=ft.icons.ADMIN_PANEL_SETTINGS,
                icon=ft.icons.ADMIN_PANEL_SETTINGS_OUTLINED,
                permission='food.admin_permission',
                workspace_data=get_admin_tiles
            ),
            PermissionNavigationRailDestination(
                label='FOOD',
                selected_icon=ft.icons.FASTFOOD,
                icon=ft.icons.FASTFOOD,
                permission='food.food_permission',
                workspace_data=get_menu_tiles
            ),
            PermissionNavigationRailDestination(
                label='CLIENTS SERVICE',
                selected_icon=ft.icons.MONEY,
                icon=ft.icons.MONEY_SHARP,
                permission='food.client_service_permission',
                workspace_data=get_clients_service_tiles
            ),
            PermissionNavigationRailDestination(
                label='COOKING',
                selected_icon=ft.icons.SOUP_KITCHEN,
                icon=ft.icons.SOUP_KITCHEN,
                permission='food.cooking_permission',
                workspace_data=get_cooking_tiles
            ),
            PermissionNavigationRailDestination(
                label='SETTINGS',
                selected_icon=ft.icons.SETTINGS,
                icon=ft.icons.SETTINGS_OUTLINED,
                permission=None,
                workspace_data=get_settings
            ),
            PermissionNavigationRailDestination(
                label='LOGOUT',
                selected_icon=ft.icons.LOGOUT,
                icon=ft.icons.LOGOUT,
                permission=None,
                workspace_data=None
            )
        ]
        self.content = ft.NavigationRail(
                indicator_color=PastelColors.MEDIUM_BROWN,
                on_change=self.change_main_menu,
                selected_index=0,
                extended=True,
                height=self.total_height,
                bgcolor=PastelColors.LIGHT_BROWN,
                label_type=ft.NavigationRailLabelType.ALL,
                leading=ft.Container(
                    ft.Text(
                        value='MENU',
                        weight=ft.FontWeight.BOLD,
                        size=20
                    )
                ),
                destinations=self.destinations
            )

    def did_mount(self):
        user_permissions = self.page.current_view.current_user.data.permissions
        for destination in self.destinations:
            if destination.permission and destination.permission not in user_permissions:
                self.destinations.remove(destination)
        self.content.destinations = self.destinations
        self.content.height = self.total_height
        self.update()

    def change_main_menu(self, e):
        if e.control.selected_index == len(self.destinations) - 1:
            self.page.dialog = LogoutDialog(logout_event=self.logout_click)
        else:
            self.page.current_view.workspace.controls.clear()
            if self.destinations[e.control.selected_index].workspace_data:
                self.page.current_view.workspace.controls = self.destinations[e.control.selected_index].workspace_data()
        self.page.update()

    def logout_click(self, _):
        self.page.current_view.auth_service.logout_user()
        if not self.page.current_view.auth_service.is_authenticated:
            self.page.go(LOGIN_PAGE_VIEW_URL)

    @property
    def total_height(self):
        return 100 + (len(self.destinations) * 40)
