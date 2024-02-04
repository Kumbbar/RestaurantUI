import flet_core as ft


class LogoutDialog(ft.AlertDialog):
    def __init__(self, logout_event):
        super().__init__()
        self.open = True
        self.modal = True
        self.logout_event = logout_event
        self.content = ft.Text("Do you really want to log out?")
        self.actions = [
            ft.TextButton("Yes", on_click=self.logout_event),
            ft.TextButton("No", on_click=self.no_click),
        ]
        self.actions_alignment = ft.MainAxisAlignment.END

    def no_click(self, _):
        self.open = False
        self.page.update()
