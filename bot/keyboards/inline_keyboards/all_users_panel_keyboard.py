from enum import IntEnum, auto

from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.keyboards.inline_keyboards.admin_panel_keyboard import AdminPanelCbData, AdminPanelActions
from db.user_db_handl import get_users


class AllUsersPanelActions(IntEnum):
    detail = auto()

    root = auto()
    next_page = auto()
    pre_page = auto()


class AllUsersPanelCbData(CallbackData, prefix='users_panel'):
    action: AllUsersPanelActions
    page: int
    total_pages: int
    chat_id: int
    name: str


def build_all_users_keyboard(page: int) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(
        text='Назад в меню',
        callback_data=AdminPanelCbData(action=AdminPanelActions.root).pack()
    )

    users = get_users()

    total_users = len(users)
    total_users_in_page = 6
    total_pages = total_users // total_users_in_page + 0 if total_users % total_users_in_page == 0 else 1

    start = (page - 1) * total_users_in_page
    stop = start + total_users_in_page

    for user in users[start:stop]:
        builder.button(
            text=user.first_name,
            callback_data=AllUsersPanelCbData(
                action=AllUsersPanelActions.detail,
                page=page,
                chat_id=user.chat_id,
                name=user.first_name,
                total_pages=total_pages
            ).pack()
        )

    if start != 0:
        builder.button(
            text='<--',
            callback_data=AllUsersPanelCbData(
                action=AllUsersPanelActions.pre_page,
                page=page,
                chat_id=0,
                name='',
                total_pages=total_pages
            ).pack()
        )

    if stop < total_users:
        builder.button(
            text='-->',
            callback_data=AllUsersPanelCbData(
                action=AllUsersPanelActions.next_page,
                page=page,
                chat_id=0,
                name='',
                total_pages=total_pages
            ).pack()
        )
    builder.adjust(1, 2)
    return builder.as_markup()
