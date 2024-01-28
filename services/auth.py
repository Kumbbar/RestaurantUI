import requests
from settings import BACKEND_BASE_URL, BACKEND_LOGIN_PATH, SESSION_TOKEN_KEY
from .base import BaseRequestService


class AuthService(BaseRequestService):
    def __set_token(self, token):
        print('set token', id(self.page_link))
        self.page_link.client_storage.set(SESSION_TOKEN_KEY, token)

    def login_user(self, username, password):
        response = requests.post(
            f'{BACKEND_BASE_URL}{BACKEND_LOGIN_PATH}',
            json=dict(username=username, password=password)
        )
        if response.status_code == 200:
            self.__set_token(response.json()[SESSION_TOKEN_KEY])

    @property
    def is_authenticated(self) -> bool:
        return self.page_link.client_storage.contains_key(SESSION_TOKEN_KEY)

    @property
    def token(self) -> str:
        return self.page_link.client_storage.get(SESSION_TOKEN_KEY)

    def logout_user(self):
        response = requests.post(
            f'{BACKEND_BASE_URL}/auth/logout/',
            headers=dict(Authorization=f'Token {self.token}')
        )
        if response.status_code == 200:
            self.page_link.client_storage.remove(SESSION_TOKEN_KEY)

