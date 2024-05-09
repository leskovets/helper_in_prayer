from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from db.user_db_handl import get_users, get_user_by_chat_id

router = Router()


@router.message(Command('users'))
async def users_view(message: Message, ) -> None:

    if not get_user_by_chat_id(message.chat.id).admin:
        return

    users = get_users()
    for user in users:
        text = f'@{user.user_name} Имя: {user.first_name}'
        await message.answer(text)
