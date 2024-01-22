import uuid
from typing import TYPE_CHECKING

from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey
from sqlalchemy.ext.hybrid import hybrid_property


from app.database import Base

if TYPE_CHECKING:
    from app.submenu.models import Submenu


class Menu(Base):
    __tablename__ = "menus"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    title: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str]
    submenus: Mapped[list["Submenu"]] = relationship(back_populates="menu1", cascade="all, delete-orphan")





