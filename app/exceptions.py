from fastapi import HTTPException, status


class MenuException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class MenuAlreadyExistsException(MenuException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Меню уже существует"


class MenuNotExistsException(MenuException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Меню не существует"


class SubmenuAlreadyExistsException(MenuException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Подменю уже существует"


class SubmenuNotExistsException(MenuException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Такого подменю не существует"


class DishAlreadyExistsException(MenuException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Блюдо уже существует"


class DishNotExistsException(MenuException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Такого блюда не существует"
