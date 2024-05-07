from aiogram.fsm.state import StatesGroup, State


class Start(StatesGroup):
    first_name = State()
    is_reminders = State()
    is_plan = State()


class RegUser(StatesGroup):
    select_user = State()
    permission = State()
    add_role = State()
    add_time = State()


class Report(StatesGroup):
    question = State()


class Reminder(StatesGroup):
    reminder_on = State()
    reminder_off = State()
    plan = State()

