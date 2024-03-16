import flet as ft


class InputDatePicker(ft.UserControl):
    def __init__(self, label):
        super().__init__()
        self.value = None
        self.date_input = ft.TextField(label=label, hint_text='Format: YYYY-MM-DD', on_change=self.date_changed)
        self.date_picker = ft.DatePicker(
            on_change=self.date_picker_changed,
            date_picker_entry_mode=ft.DatePickerEntryMode.CALENDAR_ONLY
        )
        self.content = ft.Row(
            controls=[
                self.date_input,
                ft.IconButton(
                    icon=ft.icons.CALENDAR_MONTH,
                    on_click=lambda _: self.date_picker.pick_date()
                )
            ]
        )

    def did_mount(self):
        self.page.overlay.append(self.date_picker)
        self.page.update()

    def update(self):
        self.date_input.value = self.value
        super().update()

    def date_changed(self, _):
        self.value = self.date_input.value
        self.update()

    def build(self):
        return self.content

    def date_picker_changed(self, _):
        self.date_input.value = self.date_picker.value.date()
        self.value = self.date_picker.value.date()
        self.date_input.update()
