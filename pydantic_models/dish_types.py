from typing import List

from . import BaseResponseObject, BaseResponse


class DishType(BaseResponseObject):
    name: str


class DishTypeResponse(BaseResponse):
    results: List[DishType]
