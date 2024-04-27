from enum import Enum
from typing import Callable

import requests
from requests import Response
import flet_core as ft
from flet_core import Page

from controls.bottom_sheets import BottomSheetServiceUnavailable, BottomSheetInvalidToken, ExceptionBottomSheet
from services.cryptography import decrypt_token
from services import BaseService
from settings import SESSION_TOKEN_KEY, BACKEND_BASE_URL, LOGIN_PAGE_VIEW_URL


class RequestMethod(Enum):
    GET = requests.get
    POST = requests.post
    PUT = requests.put
    DELETE = requests.delete


class BaseRequestService(BaseService):

    def __init__(self, page: Page):
        super().__init__(page)
        self.server_unavailable_response = Response()
        self.server_unavailable_response.code = "error"
        self.server_unavailable_response.error_type = "error"
        self.server_unavailable_response.status_code = 500

    def _show_server_unavailable(self):
        bottom_sheet = BottomSheetServiceUnavailable()
        self.page_link.bottom_sheet = bottom_sheet
        self.page_link.update()

    def _show_user_token_invalid(self):
        if self.page_link.route == LOGIN_PAGE_VIEW_URL:
            return
        bottom_sheet = BottomSheetInvalidToken()
        self.page_link.bottom_sheet = bottom_sheet
        self.page_link.update()

    def _show_exception(self, data):
        bottom_sheet = ExceptionBottomSheet(data)
        self.page_link.bottom_sheet = bottom_sheet
        self.page_link.update()

    def send_request(self, method: (RequestMethod, Callable), url, data=None, json=None, **kwargs) -> Response:
        try:
            return method(f'{BACKEND_BASE_URL}{url}', data=data, json=json, **kwargs)
        except requests.exceptions.ConnectionError:
            self._show_server_unavailable()
            return self.server_unavailable_response


class UserRequestService(BaseRequestService):
    def __init__(self, page: Page):
        super().__init__(page)
        self.__custom_headers = dict()

    @property
    def is_authenticated(self) -> bool:
        return self.page_link.client_storage.contains_key(SESSION_TOKEN_KEY)

    @property
    def token(self) -> str:
        if not self.page_link.client_storage.contains_key(SESSION_TOKEN_KEY):
            return ''
        encrypted_token = decrypt_token(self.page_link.client_storage.get(SESSION_TOKEN_KEY))
        return encrypted_token

    @property
    def custom_headers(self):
        return self.__custom_headers

    @custom_headers.setter
    def custom_headers(self, value):
        self.__custom_headers = value

    @property
    def all_headers(self):
        auth_headers_copy = dict(**self.auth_headers)
        auth_headers_copy.update(self.custom_headers)
        return auth_headers_copy

    @property
    def auth_headers(self):
        return dict(Authorization=f'Token {self.token}')

    def send_closed_request(self, method: (RequestMethod, Callable), url, data=None, json=None, **kwargs) -> Response:
        try:
            response: Response = method(f'{BACKEND_BASE_URL}{url}', data=data, json=json, headers=self.all_headers, **kwargs)
            if response.status_code == 401:
                self._show_user_token_invalid()
            elif response.status_code >= 400:
                self._show_exception(response.json())
            return response
        except (requests.exceptions.ConnectionError, requests.exceptions.JSONDecodeError):
            self._show_server_unavailable()
            return self.server_unavailable_response
