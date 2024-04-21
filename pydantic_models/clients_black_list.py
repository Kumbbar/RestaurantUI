from typing import List, Optional

from . import BaseResponseObject, BaseResponse


class ClientBlackList(BaseResponseObject):
    client: int


class ClientBlackListResponse(BaseResponse):
    results: List[ClientBlackList]
