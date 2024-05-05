from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def yes_no_keyboard() -> ReplyKeyboardMarkup:
    button_yes = KeyboardButton(text='Да')
    button_no = KeyboardButton(text='Нет')
    return ReplyKeyboardMarkup(keyboard=[[button_yes, button_no]], resize_keyboard=True)
