from enum import IntEnum, auto

from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


class PostponementPrayActions(IntEnum):
    postponement = auto()
    delete_message = auto()
    time = auto()
    root = auto()


class PostponementPrayCbData(CallbackData, prefix='postponement'):
    action: PostponementPrayActions
    chat_id: int
    time: int
    plan_id: int


def build_postponement_pray_keyboard(chat_id: int, plan_id: int) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(
        text='ок',
        callback_data=PostponementPrayCbData(
            action=PostponementPrayActions.delete_message,
            chat_id=chat_id,
            time=0,
            plan_id=plan_id
        ).pack()
    )
    builder.button(
        text='перенести',
        callback_data=PostponementPrayCbData(
            action=PostponementPrayActions.postponement,
            chat_id=chat_id,
            time=0,
            plan_id=plan_id
        ).pack()
    )
    builder.adjust(2)
    return builder.as_markup()


def build_postponement_pray_time_keyboard(chat_id: int, plan_id: int) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for time in (15, 30, 45, 60):
        builder.button(
            text=str(time),
            callback_data=PostponementPrayCbData(
                action=PostponementPrayActions.time,
                chat_id=chat_id,
                time=time,
                plan_id=plan_id
            ).pack()
        )
    builder.adjust(4)
    return builder.as_markup()


