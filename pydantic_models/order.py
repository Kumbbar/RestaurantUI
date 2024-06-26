import datetime
from typing import List, Optional

from . import BaseResponseObject, BaseResponse


class Order(BaseResponseObject):
    stage: str
    table: Optional[int] = None
    client: Optional[int] = None
    created_at: datetime.datetime


class OrderResponse(BaseResponse):
    results: List[Order]
