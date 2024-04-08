from typing import List, Optional

from . import BaseResponseObject, BaseResponse


class Dish(BaseResponseObject):
    name: str
    description: str
    dish_type: Optional[int] = None
    weight: int
    price: int
    image: Optional[str] = None


class DishResponse(BaseResponse):
    results: List[Dish]
