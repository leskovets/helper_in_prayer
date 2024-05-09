from datetime import time

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from bot.keyboards.keyboards.yes_no import yes_no_keyboard
from bot.utils.states import Reminder
from db.plna_db_handl import add_new_plan
from db.user_db_handl import update_user_reminder_by_chat_id, get_user_by_chat_id

router = Router()


@router.message(Command('reminder'))
async def start(message: Message, state: FSMContext) -> None:

    reminder_is_on = get_user_by_chat_id(message.chat.id).is_reminders
    if not reminder_is_on:
        text = 'Напоминания отключены. Включить?'
        await state.set_state(Reminder.reminder_on)

    else:
        text = 'Напоминания включены. Хочешь отключить?'
        await state.set_state(Reminder.reminder_off)

    await message.answer(text, reply_markup=yes_no_keyboard())


@router.message(Reminder.reminder_off, F.text.in_(('Да', 'Нет')))
async def is_reminder_on(message: Message, state: FSMContext):
    if message.text == 'Да':
        text = 'Напоминания отключены!'
        update_user_reminder_by_chat_id(message.chat.id, False)
        await message.answer(text, reply_markup=ReplyKeyboardRemove())
        await state.clear()
        return
    text = 'Введи время ЧЧ:ММ в котором планируешь молиться'
    await message.answer(text, reply_markup=ReplyKeyboardRemove())
    await state.set_state(Reminder.plan)


@router.message(Reminder.reminder_on,  F.text.in_(('Да', 'Нет')))
async def is_reminder_on(message: Message, state: FSMContext):
    if message.text == 'Нет':
        await message.answer('Ок!', reply_markup=ReplyKeyboardRemove())
        await state.clear()
        return
    update_user_reminder_by_chat_id(message.chat.id, True)
    text = 'Введи время ЧЧ:ММ в котором планируешь молиться'
    await message.answer(text, reply_markup=ReplyKeyboardRemove())
    await state.set_state(Reminder.plan)


@router.message(Reminder.reminder_off)
@router.message(Reminder.reminder_on)
async def is_reminder_on(message: Message):
    text = 'Нажми на кнопку!'
    await message.answer(text, reply_markup=yes_no_keyboard())


@router.message(Reminder.plan)
async def plan(message: Message, state: FSMContext):
    try:
        start_time = time(
            hour=int(message.text.split(':')[0]),
            minute=int(message.text.split(':')[1])
        )
    except (IndexError, ValueError):
        await message.answer('Введи время в формате ЧЧ:ММ', reply_markup=ReplyKeyboardRemove())
        return

    for day in range(7):
        add_new_plan(message.chat.id, 'pray', day, start_time)

    text = 'Отлично теперь я смогу напомнить тебе, когда у тебя молитва'
    await message.answer(text, reply_markup=ReplyKeyboardRemove())
    await state.clear()
