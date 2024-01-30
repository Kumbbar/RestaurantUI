from enum import Enum
from typing import Callable

import requests
from requests import Response
from flet_core import Page

from services.cryptography import decrypt_token
from services.base import BaseService
from settings import SESSION_TOKEN_KEY


class RequestMethod(Enum):
    GET = requests.get
    POST = requests.post
    PUT = requests.put
    DELETE = requests.delete


class BaseRequestService(BaseService):
    def send_request(self, method: (RequestMethod, Callable), url, data=None, json=None, **kwargs) -> Response:
        try:
            response = method(url, data=data, json=json, **kwargs)
            return response
        except requests.exceptions.ConnectionError:
            raise Exception


class UserRequestService(BaseRequestService):
    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def is_authenticated(self) -> bool:
        return self.page_link.client_storage.contains_key(SESSION_TOKEN_KEY)

    @property
    def token(self) -> str:
        encrypted_token = decrypt_token(self.page_link.client_storage.get(SESSION_TOKEN_KEY))
        return encrypted_token

    @property
    def headers(self):
        return dict(Authorization=f'Token {self.token}')

    def send_closed_request(self, method: (RequestMethod, Callable), url, data=None, json=None, **kwargs) -> Response:
        try:
            return method(url, data=data, json=json, headers=self.headers, **kwargs)
        except requests.exceptions.ConnectionError:
            raise Exception