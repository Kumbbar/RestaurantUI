import datetime
from typing import List, Optional

from . import BaseResponseObject, BaseResponse


class RestaurantPlanMenu(BaseResponseObject):
    menu: int
    restaurant: int
    date_start: datetime.date
    date_end: Optional[datetime.date] = None


class RestaurantPlanMenuResponse(BaseResponse):
    results: List[RestaurantPlanMenu]
