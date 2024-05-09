from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from bot.keyboards.keyboards.yes_no import yes_no_keyboard
from bot.utils.states import Start
from db.user_db_handl import add_user, get_user_by_chat_id, update_user_first_name

router = Router()


@router.message(Command('start'))
async def start(message: Message, state: FSMContext) -> None:
    user = get_user_by_chat_id(message.chat.id)
    if user is not None:
        text = f'Привет. Ты был зарегистрирован как {user.first_name}\n'\
                'Хочешь изменить имя?'
        await message.answer(text, reply_markup=yes_no_keyboard())
        await state.set_state(Start.rename)
        return
    await message.answer("Привет!!!")
    await is_rename(message, state)


@router.message(Start.rename, F.text.in_(('Да', 'Нет')))
async def is_rename(message: Message, state: FSMContext) -> None:
    if message.text == "Нет":
        text = 'Ок!\n' \
               'Ты сможешь изменить имя нажав /start'
        await message.answer(text, reply_markup=ReplyKeyboardRemove())
        await state.clear()
        return
    text = 'Введи своё имя'
    await message.answer(text, reply_markup=ReplyKeyboardRemove())
    await state.set_state(Start.first_name)


@router.message(Start.rename)
async def is_reminder_on(message: Message):
    text = 'Нажми на кнопку!'
    await message.answer(text, reply_markup=yes_no_keyboard())


@router.message(Start.first_name, F.text)
async def get_first_name(message: Message, state: FSMContext) -> None:
    if get_user_by_chat_id(message.chat.id):
        update_user_first_name(
            chat_id=message.chat.id,
            first_name=message.text
        )
    else:
        add_user(
            chat_id=message.chat.id,
            user_name=message.from_user.username,
            first_name=message.text,
        )
    text = 'Ты зарегистрирован!\n'\
           'в меню ты сможешь включить и настроить напоминания'
    await message.answer(text, reply_markup=ReplyKeyboardRemove())
    await state.clear()
