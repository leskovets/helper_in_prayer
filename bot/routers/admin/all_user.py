from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from db.story_db_handl import get_reports_lost_pray_last_week_where_chat_id
from db.user_db_handl import get_all_users

router = Router()


@router.message(Command('admin_all_users'))
async def user_view(message: Message, ) -> None:
    users = get_all_users()
    for user in users:
        story = get_reports_lost_pray_last_week_where_chat_id(user.chat_id)
        text = f'@{user.user_name} Имя:{user.first_name}\n' \
               f'id: {user.chat_id}\n'
        for day in story:
            text += f'{day.date} - {"да" if day.is_pray else "нет"}\n'
        await message.answer(text)
