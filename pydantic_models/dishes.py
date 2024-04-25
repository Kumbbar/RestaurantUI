from typing import List, Optional

from . import BaseResponseObject, BaseResponse


class Dish(BaseResponseObject):
    name: str
    description: Optional[str] = None
    dish_type: Optional[int] = None
    weight: Optional[float] = None
    price: Optional[float] = None
    image: Optional[str] = None


class DishResponse(BaseResponse):
    results: List[Dish]
