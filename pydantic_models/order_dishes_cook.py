import datetime
from typing import List, Optional

from . import BaseResponseObject, BaseResponse


class OrderDishCook(BaseResponseObject):
    count: int
    table: Optional[int] = None
    dish: int
    created_at: datetime.datetime


class OrderDishCookResponse(BaseResponse):
    results: List[OrderDishCook]
