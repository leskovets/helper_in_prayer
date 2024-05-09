from aiogram import Router

from .all_user import router as all_user_router
from .help import router as help_router
from .bad_prayers import router as bad_prayers_router
from .set_users import router as set_users_router

router = Router()

router.include_routers(
    all_user_router,
    help_router,
    bad_prayers_router,
    set_users_router
)
