from settings import BACKEND_BASE_URL, BACKEND_LOGIN_PATH, SESSION_TOKEN_KEY
from . import UserRequestService, RequestMethod
from ..cryptography import encrypt_token


class AuthService(UserRequestService):
    def __set_token(self, token: str):
        encrypted_token = encrypt_token(token)
        self.page_link.client_storage.set(SESSION_TOKEN_KEY, encrypted_token)

    def login_user(self, username, password):
        response = self.send_request(
            RequestMethod.POST,
            f'{BACKEND_BASE_URL}{BACKEND_LOGIN_PATH}',
            json=dict(username=username, password=password)
        )
        if response.ok:
            self.__set_token(response.json()[SESSION_TOKEN_KEY])

    def logout_user(self):
        response = self.send_closed_request(
            RequestMethod.POST,
            f'{BACKEND_BASE_URL}/auth/logout/',
        )
        if response.ok:
            self.page_link.client_storage.remove(SESSION_TOKEN_KEY)
