from datetime import time

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext


from bot.utils.states import Start
from db.plna_db_handl import add_new_plan
from db.user_db_handl import add_new_user
from bot.keyboards.keyboards.yes_no import yes_no_keyboard

router = Router()


@router.message(Command('start'))
async def start(message: Message, state: FSMContext) -> None:
    text = 'Привет!!!\n' \
           'Для использования бота нужно зарегистрироваться\n' \
           'Введи своё имя'
    await message.answer(text)

    await state.set_state(Start.first_name)


@router.message(Start.first_name)
async def get_first_name(message: Message, state: FSMContext) -> None:

    await state.update_data(first_name=message.text)

    text = 'Нужны ли тебе напоминания перед молитвой?'
    await message.answer(text,  reply_markup=yes_no_keyboard())

    await state.set_state(Start.is_reminders)


@router.message(Start.is_reminders)
async def get_is_reminders(message: Message, state: FSMContext) -> None:
    if message.text not in ('Да', 'Нет'):
        text = 'Нажми на кнопку!'
        await message.answer(text, reply_markup=yes_no_keyboard())
        return

    is_reminders = True if message.text == 'Да' else False

    data = await state.get_data()

    add_new_user(
        user_id=message.from_user.id,
        chat_id=message.chat.id,
        user_name=message.from_user.username,
        first_name=data['first_name'],
        is_reminders=is_reminders
    )
    for day in range(7):
        add_new_plan(
            chat_id=message.chat.id,
            type_plan='report',
            day=day,
            start_time=time(hour=23, minute=59)
        )
    text = 'Ты зарегистрирован!\n'

    if message.text == 'Да':
        text += 'зайди в меню чтобы настроить расписание напоминаний'
    else:
        text += 'в меню ты сможешь включить и настроить напоминания'
    await message.answer(text, reply_markup=ReplyKeyboardRemove())
    await state.clear()


# @router.message(Start.is_plan)
# async def get_is_plan(message: Message, state: FSMContext) -> None:
#     if message.text not in ('Да', 'Нет'):
#         text = 'Нажми на кнопку!'
#         await message.answer(text, reply_markup=yes_no_keyboard())
#         return
#
#     data = await state.get_data()
#     add_new_user(
#         user_id=message.from_user.id,
#         chat_id=message.chat.id,
#         user_name=message.from_user.username,
#         first_name=message.text,
#         is_reminders=data['is_reminders']
#     )
#
#     if message.text == 'Нет':
#         text = 'Ты зарегистрирован!'
#         await message.answer(text, reply_markup=ReplyKeyboardRemove())
#         await state.clear()
#         return
#
#     text = 'Хочешь настроить расписание молитвы?'
#     await message.answer(text, reply_markup=yes_no_keyboard())
#
#     await state.set_state(Start.is_reminders)
