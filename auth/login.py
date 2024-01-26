import requests
from settings import BACKEND_BASE_URL


def login_user(username, password):
    response = requests.post(f'{BACKEND_BASE_URL}/auth/login/', json=dict(username=username, password=password))
    if response.status_code == 200:
        return response.json()['token']
    return False
