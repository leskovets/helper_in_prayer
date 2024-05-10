from aiogram import Router

from .help import router as help_router
from .admin_panel import router as admin_router

router = Router()

router.include_routers(
    help_router,
    admin_router,
)
