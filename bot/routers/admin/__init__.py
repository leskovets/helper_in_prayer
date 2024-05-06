from aiogram import Router

from .all_user import router as all_user_router
from .help import router as help_router

router = Router()

router.include_routers(
    all_user_router,
    help_router,
)
