from typing import List, Optional

from . import BaseResponseObject, BaseResponse


class Client(BaseResponseObject):
    name: str
    surname: str
    patronymic: Optional[str] = None
    phone_number: str


class ClientResponse(BaseResponse):
    results: List[Client]
