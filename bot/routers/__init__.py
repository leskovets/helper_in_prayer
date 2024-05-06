__all__ = ('router', )

from aiogram import Router

from .commands import router as commands_router
from .surveys import router as surveys_router
from .callback_handlers import router as callback_handlers_router
from .admin import router as admin_router

router = Router()
router.include_routers(
    commands_router,
    surveys_router,
    callback_handlers_router,
    admin_router
)
