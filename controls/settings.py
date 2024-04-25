import math

import flet_core as ft

from consts.colors import PastelColors
from controls.bottom_sheets import BottomSheetDefaultWorkspace
from services.requests import RequestMethod
from settings import DEFAULT_WORKSPACE_KEY


class SettingsContainer(ft.Container):
    def __init__(self):
        super().__init__()
        self.border_radius = 10
        self.padding = ft.Padding(10, 10, 10, 20)
        self.bgcolor = ft.colors.AMBER_50
        self.alignment = ft.alignment.center
        self.default_workspace = ft.NavigationRail(
            indicator_color=PastelColors.LIGHT_BROWN,
            label_type=ft.NavigationRailLabelType.ALL,
            bgcolor=PastelColors.SEA_GREEN,
            on_change=self.change_default_workspace
        )

        self.content = ft.Column(
            [
                ft.Text('Default workspace', col=12, weight=ft.FontWeight.BOLD, size=15,
                        text_align=ft.TextAlign.CENTER),
                self.default_workspace
            ],
            alignment=ft.alignment.center
        )
        self.bgcolor = PastelColors.SEA_GREEN

    @property
    def total_height(self):
        return 100 + (len(self.default_workspace.destinations) * 40)

    def did_mount(self):
        for destination in self.page.current_view.main_menu.destinations[:-2]:
            self.default_workspace.destinations.append(
                ft.NavigationRailDestination(label=destination.label, icon=destination.icon))
        self.default_workspace.height = self.total_height

        if self.page.client_storage.contains_key(DEFAULT_WORKSPACE_KEY):
            default_key = self.page.client_storage.get(DEFAULT_WORKSPACE_KEY)
            for destination in self.default_workspace.destinations:
                if destination.label == default_key:
                    self.default_workspace.selected_index = self.default_workspace.destinations.index(destination)
        self.update()

    def change_default_workspace(self, e):
        self.page.client_storage.set(
            DEFAULT_WORKSPACE_KEY,
            self.default_workspace.destinations[e.control.selected_index].label
        )
        self.page.bottom_sheet = BottomSheetDefaultWorkspace(
            self.default_workspace.destinations[e.control.selected_index].label
        )
        self.page.update()

