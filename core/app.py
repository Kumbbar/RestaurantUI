from flet_core import Page

from settings import MAIN_PAGE_VIEW_URL
from .route import BasePageRouteHandler


class BaseApp(BasePageRouteHandler):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page.fonts = {
            "SF Pro Bold": "fonts/SFProText-Bold.ttf",
            "SF Pro Heavy": "fonts/SFProText-Heavy.ttf",
            "SF Pro HeavyItalic": "fonts/SFProText-HeavyItalic.ttf",
            "SF Pro Light": "fonts/SFProText-Light.ttf",
            "SF Pro Medium": "fonts/SFProText-Medium.ttf",
            "SF Pro Regular": "fonts/SFProText-Regular.ttf",
            "SF Pro Semibold": "fonts/SFProText-Semibold.ttf",
            "SF Pro SemiboldItalic": "fonts/SFProText-SemiboldItalic.ttf",

            "Poppins ThinItalic": "fonts/poppins/Poppins-ThinItalic.ttf",
            "Poppins Thin": "fonts/poppins/Poppins-Thin.ttf",
            "Poppins Semibold": "fonts/poppins/Poppins-Semibold.ttf",
            "Poppins SemiboldItalic": "fonts/poppins/Poppins-SemiboldItalic.ttf",
            "Poppins Regular": "fonts/poppins/Poppins-Regular.ttf",
            "Poppins MediumItalic": "fonts/poppins/Poppins-MediumItalic.ttf",
            "Poppins Medium": "fonts/poppins/Poppins-Medium.ttf",
            "Poppins LightItalic": "fonts/poppins/Poppins-LightItalic.ttf",
            "Poppins Light": "fonts/poppins/Poppins-Light.ttf",
            "Poppins Italic": "fonts/poppins/Poppins-Italic.ttf",
            "Poppins ExtraLightItalic": "fonts/poppins/Poppins-ExtraLightItalic.ttf",
            "Poppins ExtraLight": "fonts/poppins/Poppins-ExtraLight.ttf",
            "Poppins ExtraBold": "fonts/poppins/Poppins-ExtraBold.ttf",
            "Poppins ExtraBoldItalic": "fonts/poppins/Poppins-ExtraBoldItalic.ttf",
            "Poppins BoldItalic": "fonts/poppins/Poppins-BoldItalic.ttf",
            "Poppins Bold": "fonts/poppins/Poppins-Bold.ttf",
            "Poppins BlackItalic": "fonts/poppins/Poppins-BlackItalic.ttf",
            "Poppins Black": "fonts/poppins/Poppins-Black.ttf",
        }

        self.init()

    def init(self):
        self.page.go(MAIN_PAGE_VIEW_URL)
