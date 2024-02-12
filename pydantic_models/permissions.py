from typing import List

from . import BaseResponseObject, BaseResponse


class Permission(BaseResponseObject):
    name: str
    content_type: int
    codename: str


class PermissionResponse(BaseResponse):
    results: List[Permission]
