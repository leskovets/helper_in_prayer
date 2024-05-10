from enum import auto, IntEnum

from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


class AdminPanelActions(IntEnum):
    all_user = auto()
    bad_users = auto()
    admins = auto()

    root = auto()


class AdminPanelCbData(CallbackData, prefix='admin_panel'):
    action: AdminPanelActions


def build_admin_panel_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Пользователи",
        callback_data=AdminPanelCbData(
            action=AdminPanelActions.all_user,
        ).pack()
    )
    builder.button(
        text="Штрафники",
        callback_data=AdminPanelCbData(
            action=AdminPanelActions.bad_users
        ).pack()
    )
    builder.button(
        text="Админы",
        callback_data=AdminPanelCbData(
            action=AdminPanelActions.admins
        ).pack()
    )
    builder.adjust(1)
    return builder.as_markup()
