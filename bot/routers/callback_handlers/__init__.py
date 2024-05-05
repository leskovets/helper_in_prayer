__all__ = ('router', )

from aiogram import Router

from .report_pray_callback import router as report_pray_callback_router

router = Router(name=__name__)

router.include_routers(
    report_pray_callback_router,
)