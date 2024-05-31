from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.keyboards.inline_keyboards.all_users_panel_keyboard import AllUsersPanelCbData, AllUsersPanelActions


def build_user_delete_keyboard(page: int, total_pages: int, chat_id: int, name: str) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(
        text='Да',
        callback_data=AllUsersPanelCbData(
            action=AllUsersPanelActions.detail,
            page=page,
            chat_id=chat_id,
            name=name,
            total_pages=total_pages
        ).pack()
    )
    builder.button(
        text='Нет',
        callback_data=AllUsersPanelCbData(
            action=AllUsersPanelActions.detail,
            page=page,
            chat_id=chat_id,
            name=name,
            total_pages=total_pages
        ).pack()
    )
    builder.adjust(1)
    return builder.as_markup()
