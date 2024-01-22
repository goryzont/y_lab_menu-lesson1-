from uuid import UUID

from sqlalchemy import select, update, insert

from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.dishes.models import Dish
from app.dishes.schemas import SDishes


class DishDAO(BaseDAO):
    model = Dish

    @classmethod
    async def update(cls, dish_id: UUID, dish: SDishes):
        async with async_session_maker() as session:
            query = update(cls.model).filter_by(id=dish_id).values(title=dish.title, description=dish.description,
                                                                   price=dish.price)
            await session.execute(query)
            await session.commit()


