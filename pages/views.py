from flet_core import View


class StyleView(View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.padding = 0
