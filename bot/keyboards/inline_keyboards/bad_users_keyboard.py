from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.keyboards.inline_keyboards.admin_panel_keyboard import AdminPanelCbData, AdminPanelActions


def build_bad_users_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(
        text='Назад в меню',
        callback_data=AdminPanelCbData(action=AdminPanelActions.root).pack()
    )
    return builder.as_markup()
