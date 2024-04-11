from typing import List

from . import BaseResponseObject, BaseResponse


class OrderStage(BaseResponseObject):
    name: str


class OrderStageResponse(BaseResponse):
    results: List[OrderStage]
