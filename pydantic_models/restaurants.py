import datetime
from typing import List, Optional

from . import BaseResponseObject, BaseResponse


class Restaurant(BaseResponseObject):
    name: str
    boss: Optional[int] = None
    latitude: float
    longitude: float
    date_of_open: Optional[datetime.date] = None


class RestaurantResponse(BaseResponse):
    results: List[Restaurant]
