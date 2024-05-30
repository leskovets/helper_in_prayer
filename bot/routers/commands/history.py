from datetime import date

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from db.story_db_handl import get_reports_last_month_by_chat_id
from db.models import Story

router = Router()


@router.message(Command('history'))
async def start(message: Message, ) -> None:
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

    story: list[Story] = get_reports_last_month_by_chat_id(message.chat.id)
    text = ''
    for day in story:
        pray_date = date(month=day.date.month, day=day.date.day, year=day.date.year)
        pray_day = pray_date.strftime("%d")
        pray_month = months[pray_date.strftime("%m")]
        text += f'{pray_day} {pray_month} - {pray[day.is_pray]}\n'

    await message.answer(text)
