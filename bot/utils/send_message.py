from datetime import datetime, time, timedelta

from aiogram import Bot

from bot.keyboards.inline_keyboards.postponement_pray_keyboard import build_postponement_pray_keyboard


async def prayer_reminder(chat_id: int, bot: Bot, start_time: time, plan_id: int):

    time_now = datetime.now()
    time_now = timedelta(hours=time_now.hour, minutes=time_now.minute)
    start_time = timedelta(hours=start_time.hour, minutes=start_time.minute)
    lost_time = start_time - time_now

    text = f'Привет до начала молитвы осталось {int(lost_time.total_seconds() // 60)} минут'
    await bot.send_message(chat_id, text, reply_markup=build_postponement_pray_keyboard(chat_id, plan_id))
