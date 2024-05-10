from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from db.user_db_handl import get_user_by_chat_id
from bot.keyboards.inline_keyboards.admin_panel_keyboard import build_admin_panel_keyboard

router = Router()


@router.message(Command('admin'))
async def admin_panel(message: Message, ) -> None:

    if not get_user_by_chat_id(message.chat.id).admin:
        return

    await message.answer(text="Меню администратора:", reply_markup=build_admin_panel_keyboard())
