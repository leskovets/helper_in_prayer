from aiogram import F, Router
from aiogram.types import CallbackQuery

from bot.keyboards.inline_keyboards.user_detail_keyboard import build_user_detail_keyboard
from bot.keyboards.inline_keyboards.all_users_panel_keyboard import AllUsersPanelActions, AllUsersPanelCbData, \
    build_all_users_keyboard

router = Router(name=__name__)


