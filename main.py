import logging

from flet_core import Page
from flet_core.types import AppView
from flet_runtime import app

from core.app import BaseApp
import settings


class MainApp(BaseApp):
    def __init__(self, page: Page):
        super().__init__(page)


if settings.DEBUG:
    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger("flet_core").setLevel(logging.FATAL)

app(
    target=MainApp,
    view=AppView.FLET_APP_WEB,
    assets_dir='assets',
    host='127.0.0.1', port=10000
)
