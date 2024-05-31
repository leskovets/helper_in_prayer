from enum import IntEnum, auto

from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.keyboards.inline_keyboards.all_users_panel_keyboard import AllUsersPanelCbData, AllUsersPanelActions


class UserDetailActions(IntEnum):
    root = auto()
    detail = auto()
    delete = auto()
    delete_yes = auto()
    update = auto()
    archive = auto()
    history = auto()


class UserDetailCbData(CallbackData, prefix='user_detail'):
    action: UserDetailActions
    page: int
    total_pages: int
    chat_id: int
    name: str


def build_user_detail_keyboard(page: int, total_pages: int, chat_id: int, name: str) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(
        text='Назад к пользователям',
        callback_data=AllUsersPanelCbData(
            action=AllUsersPanelActions.root,
            page=page,
            chat_id=0,
            name='',
            total_pages=total_pages
        ).pack()
    )
    builder.button(
        text='Детали',
        callback_data=UserDetailCbData(
            action=UserDetailActions.detail,
            page=page,
            chat_id=chat_id,
            name=name,
            total_pages=total_pages
        ).pack()
    )
    builder.button(
        text='История',
        callback_data=UserDetailCbData(
            action=UserDetailActions.history,
            page=page,
            chat_id=chat_id,
            name=name,
            total_pages=total_pages
        ).pack()
    )
    builder.button(
        text='Обновить',
        callback_data=UserDetailCbData(
            action=UserDetailActions.update,
            page=page,
            chat_id=chat_id,
            name=name,
            total_pages=total_pages
        ).pack()
    )
    builder.button(
        text='Архивировать',
        callback_data=UserDetailCbData(
            action=UserDetailActions.archive,
            page=page,
            chat_id=chat_id,
            name=name,
            total_pages=total_pages
        ).pack()
    )
    builder.button(
        text='Удалить',
        callback_data=UserDetailCbData(
            action=UserDetailActions.delete,
            page=page,
            chat_id=chat_id,
            name=name,
            total_pages=total_pages
        ).pack()
    )

    builder.adjust(1)
    return builder.as_markup()
