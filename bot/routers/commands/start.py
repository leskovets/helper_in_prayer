from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext


from bot.utils.states import Start
from db.user_db_handl import add_user, get_user_by_chat_id

router = Router()


@router.message(Command('start'))
async def start(message: Message, state: FSMContext) -> None:
    user = get_user_by_chat_id(message.chat.id)
    if user is not None:
        text = f"Привет. Ты был зарегистрирован как {user.first_name}"
        await message.answer(text)
        return
    text = 'Привет!!!\n' \
           'Для использования бота нужно зарегистрироваться\n' \
           'Введи своё имя'
    await message.answer(text)

    await state.set_state(Start.first_name)


@router.message(Start.first_name)
async def get_first_name(message: Message, state: FSMContext) -> None:

    add_user(
        chat_id=message.chat.id,
        user_name=message.from_user.username,
        first_name=message.text,
    )
    text = 'Ты зарегистрирован!\n'\
           'в меню ты сможешь включить и настроить напоминания'
    await message.answer(text, reply_markup=ReplyKeyboardRemove())
    await state.clear()
