import uuid
from typing import TYPE_CHECKING

from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey
from sqlalchemy.ext.hybrid import hybrid_property

from app.database import Base

if TYPE_CHECKING:
    from app.menu.models import Menu
    from app.dishes.models import Dish


class Submenu(Base):
    __tablename__ = "submenus"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    title: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str]
    menu_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('menus.id', ondelete="CASCADE"))

    menu1: Mapped["Menu"] = relationship(back_populates="submenus")
    dishes: Mapped[list["Dish"]] = relationship(back_populates="submenu", cascade="all, delete-orphan")


