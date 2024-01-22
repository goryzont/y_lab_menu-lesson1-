from uuid import UUID

from pydantic import BaseModel


class SMenu(BaseModel):

    id: UUID
    submenu: UUID
    title: str
    description: str
    submenus_count: int
    dishes_count: int

    class Config:
        from_attributes = True


class SPathMenu(BaseModel):
    title: str
    description: str


class Response(BaseModel):
    code: str
    status: str
    message: str
