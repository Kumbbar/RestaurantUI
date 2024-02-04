import flet_core as ft

from consts.colors import PastelColors
from controls.dialogs import LogoutDialog
from core.tiles_list import get_admin_tiles
from settings import LOGIN_PAGE_VIEW_URL


class MainMenu(ft.Container):
    def __init__(self):
        super().__init__()
        self.col = {
                "xs": 0,
                "sm": 3.8,
                "md": 3,
                "xl": 3
        }
        self.border_radius = 10

        self.destinations = [
                    ft.NavigationRailDestination(
                        label='ADMIN',
                        selected_icon=ft.icons.ADMIN_PANEL_SETTINGS,
                        icon=ft.icons.ADMIN_PANEL_SETTINGS_OUTLINED,
                    ),
                    ft.NavigationRailDestination(
                        label='MENU',
                        selected_icon=ft.icons.MENU_BOOK_SHARP,
                        icon=ft.icons.MENU_BOOK,
                    ),
                    ft.NavigationRailDestination(
                        label='SETTINGS',
                        selected_icon=ft.icons.SETTINGS,
                        icon=ft.icons.SETTINGS_OUTLINED,
                    ),
                    ft.NavigationRailDestination(
                        label='LOGOUT',
                        selected_icon=ft.icons.TAG,
                        icon=ft.icons.LOGOUT,
                    )
                ]
        self.content = ft.NavigationRail(
                indicator_color=PastelColors.MEDIUM_BROWN,
                on_change=self.change_main_menu,
                selected_index=0,
                extended=True,
                height=self.total_height,
                bgcolor=PastelColors.DARK_BROWN,
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

    def change_main_menu(self, e):
        if e.control.selected_index == 0:
            self.page.current_view.workspace.controls.clear()
            self.page.current_view.workspace.controls = get_admin_tiles()
        if e.control.selected_index == 3:
            self.page.dialog = LogoutDialog(logout_event=self.logout_click)
        self.page.update()

    def logout_click(self, _):
        self.page.current_view.auth_service.logout_user()
        if not self.page.current_view.auth_service.is_authenticated:
            self.page.go(LOGIN_PAGE_VIEW_URL)

    @property
    def total_height(self):
        return 100 + (len(self.destinations) * 40)
