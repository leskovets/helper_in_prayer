__all__ = ('router', )

from aiogram import Router

from .report_pray_callback import router as report_pray_callback_router
from .admin_panel_callback import router as admin_panel_callback_router
from .all_users_panel_callback import router as all_users_panel_callback_router
from .bad_users_callback import router as bad_users_callback_router
from .postponement_pray_callback import router as postponement_pray_callback_router
from .user_detail_callback import router as user_detail_callback_router

router = Router(name=__name__)

router.include_routers(
    report_pray_callback_router,
    admin_panel_callback_router,
    all_users_panel_callback_router,
    bad_users_callback_router,
    postponement_pray_callback_router,
    user_detail_callback_router,
)
