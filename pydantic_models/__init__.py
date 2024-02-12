from pydantic import BaseModel


class BaseResponseObject(BaseModel):
    id: int


class BaseResponse(BaseModel):
    count: int
