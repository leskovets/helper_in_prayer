from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def is_pray_markup(date: str) -> InlineKeyboardMarkup:
    yes_bt = InlineKeyboardButton(text='yes', callback_data=f'is_pray_True_{date}')
    no_bt = InlineKeyboardButton(text='no', callback_data=f'is_pray_False_{date}')
    markup = InlineKeyboardMarkup(inline_keyboard=[[yes_bt, no_bt]])
    return markup

