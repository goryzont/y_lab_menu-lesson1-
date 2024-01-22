import uuid
from typing import TYPE_CHECKING

from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey


from app.database import Base

if TYPE_CHECKING:
    from app.submenu.models import Submenu


class Dish(Base):
    __tablename__ = 'dishes'

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    title: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str]
    price: Mapped[float]
    submenu_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("submenus.id", ondelete="CASCADE"))

    submenu: Mapped["Submenu"] = relationship(back_populates="dishes")


