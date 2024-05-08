from datetime import time

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from bot.keyboards.keyboards.yes_no import yes_no_keyboard
from bot.utils.states import Reminder
from db.plna_db_handl import add_new_plan
from db.user_db_handl import check_reminder_by_chat_id, update_user_reminder_by_chat_id

router = Router()


@router.message(Command('reminder'))
async def start(message: Message, state: FSMContext) -> None:

    if not check_reminder_by_chat_id(message.chat.id):
        await message.answer('У тебя не в включены напоминания. Включить?', reply_markup=yes_no_keyboard())
        await state.update_data(is_reminder=True)
    else:
        text = 'Хочешь отключить напоминание?'
        await message.answer(text, reply_markup=yes_no_keyboard())
        await state.update_data(is_reminder=False)

    await state.set_state(Reminder.reminder_on)


@router.message(Reminder.reminder_on)
async def is_reminder_(message: Message, state: FSMContext):
    try:
        if message.text not in ('Да', 'Нет'):
            raise ValueError()
    except ValueError:
        text = 'Нажми на кнопку!'
        await message.answer(text, reply_markup=yes_no_keyboard())
        return

    is_reminder = await state.get_data()

    if is_reminder['is_reminder'] is False:

        text = 'Напоминания отключены!'
        update_user_reminder_by_chat_id(message.chat.id, False)
        await message.answer(text, reply_markup=ReplyKeyboardRemove())
        await state.clear()
        return

    update_user_reminder_by_chat_id(message.chat.id, True)
    await message.answer('Введи время ЧЧ:ММ в котором планируешь молиться', reply_markup=ReplyKeyboardRemove())
    await state.set_state(Reminder.plan)


@router.message(Reminder.plan)
async def plan(message: Message, state: FSMContext):
    try:
        start_time = time(
            hour=int(message.text.split(':')[0]),
            minute=int(message.text.split(':')[1])
        )
    except (IndexError, ValueError):
        await message.answer('Введи время ЧЧ:ММ', reply_markup=ReplyKeyboardRemove())
        return

    for day in range(7):
        add_new_plan(message.chat.id, 'pray', day, start_time)

    text = 'Время добавлено'
    await message.answer(text, reply_markup=ReplyKeyboardRemove())
    await state.clear()
