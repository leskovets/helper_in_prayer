from datetime import date

from aiogram import F, Router
from aiogram.types import CallbackQuery

from bot.keyboards.inline_keyboards.admin_panel_keyboard import build_admin_panel_keyboard
from bot.keyboards.inline_keyboards.user_delete_keyboard import build_user_delete_keyboard
from bot.keyboards.inline_keyboards.user_detail_keyboard import UserDetailActions, UserDetailCbData
from bot.keyboards.inline_keyboards.uesr_history_keyboard import build_user_history_keyboard
from db.story_db_handl import get_reports_last_month_by_chat_id

from db.models import Story
from db.user_db_handl import del_user_by_chat_id

router = Router(name=__name__)


@router.callback_query(
    UserDetailCbData.filter(F.action == UserDetailActions.history)
)
async def handel_user_detail_history(call: CallbackQuery, callback_data: UserDetailCbData):

    pray = {
        1: 'молился',
        0: 'не молился'
    }

    months = {
        '01': 'Января',
        '02': 'Февраля',
        '03': 'Марта',
        '04': 'Апреля',
        '05': 'Мая',
        '06': 'Июня',
        '07': 'Июля',
        '08': 'Августа',
        '09': 'Сентября',
        '10': 'Октября',
        '11': 'Ноября',
        "12": 'Декабря'
    }

    story: list[Story] = get_reports_last_month_by_chat_id(callback_data.chat_id)
    text = ''
    for day in story:
        pray_date = date(month=day.date.month, day=day.date.day, year=day.date.year)
        pray_day = pray_date.strftime("%d")
        pray_month = months[pray_date.strftime("%m")]
        text += f'{pray_day} {pray_month} - {pray[day.is_pray]}\n'

    await call.message.edit_text(
        text=text,
        reply_markup=build_user_history_keyboard(
            page=callback_data.page,
            total_pages=callback_data.total_pages,
            chat_id=callback_data.chat_id,
            name=callback_data.name)
        )


@router.callback_query(
    UserDetailCbData.filter(F.action == UserDetailActions.delete)
)
async def handel_user_delete(call: CallbackQuery, callback_data: UserDetailCbData):

    text = 'Удалить пользователя?'
    await call.message.edit_text(
        text=text,
        reply_markup=build_user_delete_keyboard(
            page=callback_data.page,
            total_pages=callback_data.total_pages,
            chat_id=callback_data.chat_id,
            name=callback_data.name)
        )


@router.callback_query(
    UserDetailCbData.filter(F.action == UserDetailActions.delete_yes)
)
async def handel_user_delete(call: CallbackQuery, callback_data: UserDetailCbData):
    del_user_by_chat_id(callback_data.chat_id)
    await call.message.edit_text(text="Меню администратора:", reply_markup=build_admin_panel_keyboard())
