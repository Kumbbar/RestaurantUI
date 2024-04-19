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


class InputTimePicker(ft.UserControl):
    def __init__(self, label):
        super().__init__()
        self.value = None
        self.time_input = ft.TextField(label=label, hint_text='Format: HH:MM:SS', on_change=self.time_changed)
        self.time_picker = ft.TimePicker(
            on_change=self.time_picker_changed,
            time_picker_entry_mode=ft.TimePickerEntryMode.DIAL
        )
        self.content = ft.Row(
            controls=[
                self.time_input,
                ft.IconButton(
                    icon=ft.icons.CALENDAR_MONTH,
                    on_click=lambda _: self.time_picker.pick_time()
                )
            ]
        )

    def did_mount(self):
        self.page.overlay.append(self.time_picker)
        self.page.update()

    def update(self):
        self.time_input.value = self.value
        super().update()

    def time_changed(self, _):
        self.value = self.time_input.value
        self.update()

    def build(self):
        return self.content

    def time_picker_changed(self, _):
        self.time_input.value = self.time_picker.value
        self.value = self.time_picker.value
        self.time_input.update()


class InputDateTimePicker(ft.UserControl):
    def __init__(self, label):
        super().__init__()
        self.date_picker = InputDatePicker('date')
        self.time_picker = InputTimePicker('time')
        self.content = ft.ResponsiveRow(
            controls=[
                ft.Text(label, weight=ft.FontWeight.BOLD, size=17),
                self.date_picker,
                self.time_picker,

            ]
        )

    @property
    def value(self):
        if self.date_picker.value and self.time_picker.value:
            return f'{self.date_picker.value} {self.time_picker.value}'
        return None

    @value.setter
    def value(self, value):
        date, time = value.split()
        self.date_picker.value = date
        self.time_picker.value = time
        self.date_picker.update()
        self.time_picker.update()

    def build(self):
        return self.content

