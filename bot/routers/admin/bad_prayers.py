from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from db.story_db_handl import get_reports_lost_pray_last_week_where_chat_id
from db.user_db_handl import get_users, get_user_by_chat_id

router = Router()


@router.message(Command('bad_users'))
async def user_view(message: Message, ) -> None:

    if not get_user_by_chat_id(message.chat.id).admin:
        return

    users = get_users()
    for user in users:
        story = get_reports_lost_pray_last_week_where_chat_id(user.chat_id)
        text = f'@{user.user_name} Имя: {user.first_name}\n'
        if story:
            for day in story:
                text += f'{day.date} - {"да" if day.is_pray else "нет"}\n'
            await message.answer(text)
