from aiogram import F, Router
from aiogram.types import CallbackQuery

from bot.keyboards.inline_keyboards.user_detail_keyboard import UserDetailActions, \
    UserDetailCbData
from bot.keyboards.inline_keyboards.all_users_panel_keyboard import AllUsersPanelActions, AllUsersPanelCbData, \
    build_all_users_keyboard

router = Router(name=__name__)


@router.callback_query(
    UserDetailCbData.filter(F.action == UserDetailActions.history)
)
async def handel_user_detail_history(call: CallbackQuery, callback_data: UserDetailCbData):
    message = ''
    await call.message.edit_text(
        text=message,
        reply_markup=...
    )