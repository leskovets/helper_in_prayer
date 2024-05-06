from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command('admin_help'))
async def start(message: Message, ) -> None:
    text = '/admin_all_users\n' \
           '/admin_del_user\n' \
           '/admin_set_user\n'
    await message.answer(text)
