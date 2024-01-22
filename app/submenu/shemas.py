from uuid import UUID

from pydantic import BaseModel


class SSubmenu(BaseModel):

    title: str
    description: str

    class Config:
        from_attributes = True


class Response(BaseModel):
    code: str
    status: str
    message: str
