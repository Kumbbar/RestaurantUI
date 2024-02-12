from typing import List

from . import BaseResponseObject, BaseResponse


class ContentType(BaseResponseObject):
    app_label: str
    model: str


class ContentTypeResponse(BaseResponse):
    results: List[ContentType]
