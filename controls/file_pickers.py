import flet_core as ft


class FileField(object):
    def __init__(self):
        self.is_file_field = True
        self.file_changed = False
        self.value = None
        super().__init__()


class FilePickerImage(FileField, ft.UserControl):
    def __init__(self):
        super().__init__()
        self.image = ft.Image(
            width=150,
            height=150,
            border_radius=10,
            fit=ft.ImageFit.COVER,
            src='assets/images/dish.svg'
        )
        self.content = ft.Container(
            height=200,
            width=150,
            content=ft.Column([
                    ft.Text('dish image'),
                    self.image
                ]
            ),
            on_click=self.image_click,
            alignment=ft.alignment.center
        )
        self.file_picker = ft.FilePicker(on_result=self.image_picked)

    def did_mount(self):
        self.page.controls.append(self.file_picker)
        self.page.update()

    def image_picked(self, e):
        if not e.files:
            return
        file = e.files[0]
        self.value = file.path
        self.file_changed = True
        self.update()

    def update(self):
        if self.value:
            self.image.src = self.value
            self.image.update()
        super().update()

    def image_click(self, _):
        self.file_picker.pick_files(allow_multiple=False, file_type=ft.FilePickerFileType.IMAGE)

    def build(self):
        return self.content
