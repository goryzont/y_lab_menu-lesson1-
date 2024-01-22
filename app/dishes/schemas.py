
from uuid import UUID

from pydantic import BaseModel


class SDishes(BaseModel):

    title: str
    description: str
    price: float

    class Config:
        from_attributes = True


class Response(BaseModel):
    code: str
    status: str
    message: str
