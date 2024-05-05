__all__ = ('router', )

from aiogram import Router

from .start import router as start_router
from .reminder import router as add_plan_router
from .help import router as help_router
from .history import router as history_router

router = Router()

router.include_routers(
    start_router,
    add_plan_router,
    help_router,
    history_router,
)
