from typing import List

from . import BaseResponseObject, BaseResponse


class UserProfileResponse(BaseResponseObject):
    username: str
    first_name: str
    last_name: str
    email: str
    is_superuser: bool
    is_staff: bool
    permissions: List[str]