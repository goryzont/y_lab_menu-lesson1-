from uuid import UUID

from sqlalchemy import update, select, func
from sqlalchemy.orm import selectinload

from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.dishes.models import Dish
from app.submenu.models import Submenu
from app.submenu.shemas import SSubmenu


class SubmenuDAO(BaseDAO):
    model = Submenu

    @classmethod
    async def update(cls, menu_id: UUID, submenu: SSubmenu):
        async with async_session_maker() as session:
            query = update(Submenu).filter_by(id=menu_id).values(title=submenu.title, description=submenu.description)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def find_all(cls, menu_id: UUID):
        async with async_session_maker() as session:
            query = select(Submenu).options(selectinload(Submenu.dishes)).filter_by(menu_id=menu_id)
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def find_by_id(cls, submenu_id: UUID, menu_id: UUID):
        async with (async_session_maker() as session):
            dishes_count = select(func.count(Dish.id)).where(Dish.submenu_id == submenu_id).label("dishes_count")
            query = select(Submenu, dishes_count
                           ).options(selectinload(Submenu.dishes)
                                     ).where(Submenu.id == submenu_id, Submenu.menu_id == menu_id)
            result = await session.execute(query)
            return result.mappings().one_or_none()

