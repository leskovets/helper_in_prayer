from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def set_user_markup(date: str) -> InlineKeyboardMarkup:
    edit_bt = InlineKeyboardButton(text='изменить', callback_data=f'edit_user_{date}')
    markup = InlineKeyboardMarkup(inline_keyboard=[[edit_bt]])
    return markup


def edit_user_markup(date: str) -> InlineKeyboardMarkup:
    set_admin_bt = InlineKeyboardButton(text='админка', callback_data=f'set_admin_{date}')
    markup = InlineKeyboardMarkup(inline_keyboard=[[set_admin_bt]])
    return markup


def set_admin_markup(date: str) -> InlineKeyboardMarkup:
    add_admin = InlineKeyboardButton(text='назначить', callback_data=f'add_admin_{date}')
    dell_admin = InlineKeyboardButton(text='удалить', callback_data=f'dell_admin_{date}')
    markup = InlineKeyboardMarkup(inline_keyboard=[[add_admin], [dell_admin]])
    return markup

