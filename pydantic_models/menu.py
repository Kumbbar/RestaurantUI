from typing import List, Optional

from . import BaseResponseObject, BaseResponse


class Menu(BaseResponseObject):
    name: str


class MenuResponse(BaseResponse):
    results: List[Menu]
