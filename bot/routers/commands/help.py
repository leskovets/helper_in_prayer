from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message


router = Router()


@router.message(Command('help'))
async def start(message: Message, ) -> None:
    text = 'Если возникли вопросы напишите мне https://t.me/leskovets_yuri'
    await message.answer(text)
