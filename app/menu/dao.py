from uuid import UUID

from sqlalchemy import update, select, func
from sqlalchemy.orm import selectinload, aliased
from sqlalchemy.sql import alias

from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.dishes.models import Dish
from app.menu.models import Menu
from app.menu.schemas import SPathMenu, SMenu

from app.submenu.models import Submenu


class MenuDAO(BaseDAO):
    model = Menu

    @classmethod
    async def update(cls, menu_id: UUID, menu: SPathMenu):
        async with async_session_maker() as session:
            query = update(cls.model).filter_by(id=menu_id).values(title=menu.title, description=menu.description)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def find_all(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(Menu).options(selectinload(Menu.submenus))
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def find_by_id(cls, model_id: UUID):
        async with (async_session_maker() as session):
            submenus_count = select(func.count(Submenu.id)).where(Submenu.menu_id == model_id).label("submenus_count")
            dishes_count = select(func.count(Dish.id)).distinct().label("dishes_count")

            query = select(Menu, submenus_count, dishes_count).options(selectinload(Menu.submenus).joinedload(Submenu.dishes)).filter_by(id=model_id)
            result = await session.execute(query)
            return result.mappings().one_or_none()


