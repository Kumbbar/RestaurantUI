from typing import List, Optional

from . import BaseResponseObject, BaseResponse


class Table(BaseResponseObject):
    number: int
    restaurant: int
    description: Optional[str] = None


class TableResponse(BaseResponse):
    results: List[Table]
