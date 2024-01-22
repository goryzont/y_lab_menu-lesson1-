from uuid import UUID

from fastapi import APIRouter, Depends

from app.exceptions import MenuAlreadyExistsException, MenuNotExistsException, SubmenuNotExistsException
from app.menu.dao import MenuDAO
from app.submenu.dao import SubmenuDAO
from app.submenu.shemas import SSubmenu, Response

router = APIRouter()


@router.get('/{target_menu_id}/submenus')
async def get_all_submenus_one_menu(menu_id: UUID):
    existing_menu = await MenuDAO.find_one_or_none(id=menu_id)
    if not existing_menu:
        raise MenuNotExistsException
    return await SubmenuDAO.find_all(menu_id=menu_id)


@router.get('/{target_menu_id}/submenus/{target_submenu_id}')
async def get_one_submenu(target_menu_id: UUID, target_submenu_id: UUID):
    existing_submenu = await SubmenuDAO.find_by_id(target_menu_id, target_submenu_id)
    if not existing_submenu:
        raise SubmenuNotExistsException
    return existing_submenu


@router.post('/{target_menu_id}/submenus', status_code=201)
async def add_submenu_for_menu(target_menu_id: UUID, title: str, description: str):
    existing_menu = await MenuDAO.find_one_or_none(id=target_menu_id)
    if not existing_menu:
        raise MenuNotExistsException
    await SubmenuDAO.add(title=title, description=description, menu_id=target_menu_id)
    return Response(code='201', status="OK", message="Create").model_dump(exclude_none=True)


@router.delete('/{target_menu_id}/submenus/{target_submenu_id}')
async def delete_submenu(submenu_id: UUID, menu_id: UUID):
    existing_submenu = await SubmenuDAO.find_by_id(submenu_id, menu_id)
    if not existing_submenu:
        raise SubmenuNotExistsException
    await SubmenuDAO.delete(submenu_id)
    return "Подменю успешно удалено"


@router.patch('/{target_menu_id}/submenus/{target_submenu_id}')
async def update_submenu(submenu_id: UUID, menu_id: UUID,  submenu: SSubmenu):
    existing_submenu = await SubmenuDAO.find_by_id(submenu_id, menu_id)
    if not existing_submenu:
        raise SubmenuNotExistsException
    await SubmenuDAO.update(submenu_id, submenu)
    return await SubmenuDAO.find_by_id(submenu_id, menu_id)


