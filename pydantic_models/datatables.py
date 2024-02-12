from typing import List

from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    first_name: str
    last_name: str
    is_staff: bool
    email: str


class UserResponse(BaseModel):
    count: int
    results: List[User]
