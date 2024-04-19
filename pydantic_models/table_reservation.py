import datetime
from typing import List, Optional

from . import BaseResponseObject, BaseResponse


class TableReservation(BaseResponseObject):
    table: int
    client: Optional[int] = None
    restaurant: int = None
    time_of_start: datetime.datetime
    time_of_end: datetime.datetime
    confirmed: bool
    has_come: bool


class TableReservationResponse(BaseResponse):
    results: List[TableReservation]
