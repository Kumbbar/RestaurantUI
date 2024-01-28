from flet_core import Page


class BaseService(object):
    def __init__(self, page: Page):
        self.page_link = page


class BaseRequestService(BaseService):
    resource_url: str
