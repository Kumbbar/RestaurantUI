from typing import List

from . import BaseResponseObject, BaseResponse


class User(BaseResponseObject):
    username: str
    first_name: str
    last_name: str
    is_staff: bool
    email: str


class UserResponse(BaseResponse):
    results: List[User]