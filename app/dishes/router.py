from uuid import UUID

from fastapi import APIRouter, Depends

from app.dishes.dao import DishDAO
from app.dishes.schemas import SDishes, Response
from app.exceptions import MenuAlreadyExistsException, MenuNotExistsException, SubmenuNotExistsException, \
    DishNotExistsException
from app.menu.dao import MenuDAO
from app.submenu.dao import SubmenuDAO
from app.submenu.shemas import SSubmenu

router = APIRouter()


@router.get('/get_all_dishes')
async def get_all_dishes(submenu_id: UUID):
    existing_submenu = await SubmenuDAO.find_one_or_none(id=submenu_id)
    if not existing_submenu:
        raise SubmenuNotExistsException
    return await DishDAO.find_all(submenu_id=submenu_id)


@router.get('/get_one_dish')
async def get_one_dish(dish_id: UUID):
    existing_dish = await DishDAO.find_one_or_none(id=dish_id)
    if not existing_dish:
        raise DishNotExistsException
    return existing_dish


@router.post('/add_dish', status_code=201)
async def add_dish(submenu_id: UUID, title: str, description: str, price: float):
    existing_submenu = await SubmenuDAO.find_one_or_none(id=submenu_id)
    if not existing_submenu:
        raise SubmenuNotExistsException
    await DishDAO.add(title=title, description=description, price=round(price, 2), submenu_id=submenu_id)
    return Response(code='201', status="OK", message="Create").model_dump(exclude_none=True)


@router.delete('/delete_dish')
async def delete_dish(dish_id: UUID):
    existing_dish = await DishDAO.find_by_id(id=dish_id)
    if not existing_dish:
        raise DishNotExistsException
    await DishDAO.delete(dish_id)
    return "Блюдо успешно удалено"


@router.patch('/update_dish')
async def update_dish(dish_id: UUID, dish: SDishes):
    existing_dish = await DishDAO.find_by_id(id=dish_id)
    if not existing_dish:
        raise DishNotExistsException
    await DishDAO.update(dish_id, dish)
    return await DishDAO.find_by_id(id=dish_id)


