from flet import *
import logging

from core.app import BaseApp
import settings


class MainApp(BaseApp):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page.dark_theme = False


if settings.DEBUG:
    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger("flet_core").setLevel(logging.INFO)

app(target=MainApp, view=WEB_BROWSER, assets_dir='assets', host='127.0.0.1', port=10000)
