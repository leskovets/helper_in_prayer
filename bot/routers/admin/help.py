from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from db.user_db_handl import get_user_by_chat_id

router = Router()


@router.message(Command('a_help'))
async def admin_help(message: Message, ) -> None:
    if not get_user_by_chat_id(message.chat.id).admin:
        return

    text = '/admin\n' \
           '/\n' \
           '/\n'
    await message.answer(text)
