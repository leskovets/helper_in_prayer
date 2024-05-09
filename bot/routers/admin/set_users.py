from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from db.user_db_handl import get_users, get_user_by_chat_id
from bot.keyboards.inline_keyboards.set_user import set_user_markup

router = Router()


@router.message(Command('set_users'))
async def set_user(message: Message, ) -> None:

    # if not get_user_by_chat_id(message.chat.id).admin:
    #     return

    users = get_users()
    for user in users:
        text = f'@{user.user_name} Имя: {user.first_name}'
        await message.answer(text, reply_markup=set_user_markup(user.chat_id))
