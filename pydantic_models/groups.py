from typing import List

from . import BaseResponseObject, BaseResponse


class Group(BaseResponseObject):
    name: str


class GroupResponse(BaseResponse):
    results: List[Group]
