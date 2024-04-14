import datetime
from typing import List, Optional

from . import BaseResponseObject, BaseResponse


class OrderDish(BaseResponseObject):
    stage: str
    count: int
    order: int
    dish: int


class OrderDishResponse(BaseResponse):
    results: List[OrderDish]
