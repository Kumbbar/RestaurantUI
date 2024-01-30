import os

from dotenv import load_dotenv

# Load .env file
load_dotenv()

DEBUG = True

# Backend settings
HTTP_METHOD = 'http'
BACKEND_DOMAIN = '127.0.0.1'
BACKEND_PORT = '8000'
BACKEND_BASE_URL = f'{HTTP_METHOD}://{BACKEND_DOMAIN}:{BACKEND_PORT}'
BACKEND_LOGIN_PATH = '/auth/login/'

# UI app settings
MAIN_PAGE_VIEW_URL = '/'
LOGIN_PAGE_VIEW_URL = '/login'

SESSION_TOKEN_KEY = 'token'


SECRET_KEY = os.environ.get('SECRET_KEY')
