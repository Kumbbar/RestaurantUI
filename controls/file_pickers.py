import flet_core as ft


class FileField(object):
    def __init__(self):
        self.is_file_field = True
        self.file_changed = False
        super().__init__()


class FilePickerImage(FileField, ft.UserControl):
    def __init__(self):
        super().__init__()
        self.value = None
        self.image = ft.Image(
            width=200,
            height=200,
            border_radius=10
        )
        self.content = ft.Container(
            height=200,
            width=200,
            content=self.image,
            on_click=self.image_click,
            alignment=ft.alignment.center
        )
        self.file_picker = ft.FilePicker(on_result=self.image_picked)

    def did_mount(self):
        self.page.controls.append(self.file_picker)
        self.page.update()

    def image_picked(self, e):
        file = e.files[0]
        self.value = file.path
        self.file_changed = True
        self.update()

    def update(self):
        self.image.src = self.value
        self.image.update()
        super().update()

    def image_click(self, _):
        self.file_picker.pick_files(allow_multiple=False, file_type=ft.FilePickerFileType.IMAGE)

    def build(self):
        return self.content