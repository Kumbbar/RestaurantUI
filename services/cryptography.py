from settings import SECRET_KEY
from flet.security import encrypt, decrypt


def decrypt_token(token: str):
    decrypted_token = decrypt(token, SECRET_KEY)
    return decrypted_token


def encrypt_token(token: str):
    encrypted_token = encrypt(token, SECRET_KEY)
    return encrypted_token
