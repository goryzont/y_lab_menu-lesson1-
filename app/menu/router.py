from uuid import UUID

from fastapi import APIRouter, Depends

from app.exceptions import MenuAlreadyExistsException, MenuNotExistsException
from app.menu.dao import MenuDAO
from app.menu.schemas import SMenu, SPathMenu, Response

router = APIRouter()


@router.get('/')
async def get_all_menus():
    return await MenuDAO.find_all()


@router.get('/{target_menu_id}')
async def get_menu(menu_id: UUID):
    return await MenuDAO.find_by_id(menu_id)


@router.post('/', status_code=201)
async def add_menu(title: str, description: str):
    existing_menu = await MenuDAO.find_one_or_none(title=title)
    if existing_menu:
        raise MenuAlreadyExistsException
    await MenuDAO.add(title=title, description=description)
    return Response(code='201', status="OK", message="Create").model_dump(exclude_none=True)


@router.delete('/{target_menu_id}')
async def delete_menu(target_menu_id: UUID):
    existing_menu = await MenuDAO.find_by_id(target_menu_id)
    if not existing_menu:
        raise MenuNotExistsException
    await MenuDAO.delete(target_menu_id)
    return "Меню успешно удалено"


@router.patch('/{target_menu_id}')
async def update_menu(target_menu_id: UUID, menu: SPathMenu):
    existing_menu = await MenuDAO.find_by_id(target_menu_id)
    if not existing_menu:
        raise MenuNotExistsException
    await MenuDAO.update(target_menu_id, menu)
    return await MenuDAO.find_by_id(target_menu_id)



