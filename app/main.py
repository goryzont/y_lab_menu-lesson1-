from fastapi import FastAPI

from app.menu.router import router as router_menu
from app.submenu.router import router as router_submenu
from app.dishes.router import router as router_dishes

app = FastAPI(
    title="Y_LAB_1",
)

app.include_router(router_menu, prefix="/api/v1/menus", tags=["menu"])
app.include_router(router_submenu, prefix="/api/v1/menus", tags=["submenu"])
app.include_router(router_dishes, prefix="/api/v1/menus", tags=["dishes"])