from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from db.story_db_handl import add_report_pray

router = Router()


@router.message(Command('help'))
async def start(message: Message, ) -> None:
    text = 'Если возникли вопросы напишите мне https://t.me/leskovets_yuri'
    await message.answer(text)
