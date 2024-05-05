import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from aiogram.types import BotCommand


async def bot_init() -> tuple[Bot, Dispatcher]:
    load_dotenv('.env')

    token = os.getenv('API_TOKEN')
    bot = Bot(token)
    await bot.set_my_commands([
        BotCommand(command='help', description='Помощь'),
        BotCommand(command='reminder', description='Напоминания'),
        BotCommand(command='story', description='История молитв'),

    ])
    dp = Dispatcher()

    return bot, dp
