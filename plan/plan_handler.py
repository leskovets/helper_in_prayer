import asyncio
from datetime import date, datetime, timedelta
from collections import Counter

from aiogram import Bot

from db.plna_db_handl import get_immediate_plans, update_all_total_alarm_to_false
from db.story_db_handl import add_report_pray, get_reports_false_pray_last_week
from db.user_db_handl import get_all_users
from db.models import Story
from bot.utils.send_message import prayer_reminder
from bot.keyboards.inline_keyboards.is_pray import is_pray_markup


async def check_reminders(bot: Bot, await_time: int = 60) -> None:
    """
    :param bot: bot
    :param await_time: time in seconds for awaiting
    """
    while True:
        plans = get_immediate_plans('pray')
        for plan in plans:
            await prayer_reminder(plan.chat_id, bot, plan.time)

        await asyncio.sleep(await_time)


async def check_pray(bot: Bot, await_time: int = 60 * 4) -> None:
    """
    :param bot: bot
    :param await_time: time in seconds for awaiting
    """

    months = {
        '01': 'Января',
        '02': 'Февраля',
        '03': 'Марта',
        '04': 'Апреля',
        '05': 'Мая',
        '06': 'Июня',
        '07': 'Июля',
        '08': 'Августа',
        '09': 'Сентября',
        '10': 'Октября',
        '11': 'Ноября',
        "12": 'Декабря'
    }
    while True:

        time_now = timedelta(
            hours=datetime.now().hour,
            minutes=datetime.now().minute
        )

        if timedelta(hours=23, minutes=55) < time_now:

            today_date = date.today().strftime("%d ")
            today_date += months[date.today().strftime("%m")]
            users = get_all_users()

            for user in users:
                add_report_pray(user.chat_id, False, date.today())
                await bot.send_message(
                    user.chat_id,
                    f'Помолился ли ты {today_date}?',
                    reply_markup=is_pray_markup(date.today().strftime('%d %m %Y'))
                )

            # await = 23 hours and 50 min
            await_time = (60 * 60 * 24) - 60 * 10

        await asyncio.sleep(await_time)


async def restart_reminder_status(await_time: int = 60 * 29) -> None:
    """
    param await_time: time in seconds for awaiting
    """
    while True:
        time_now = timedelta(
            hours=datetime.now().hour,
            minutes=datetime.now().minute
        )
        week_day_now = datetime.weekday(datetime.now())

        if (timedelta(hours=23, minutes=55) < time_now) and week_day_now == 6:
            update_all_total_alarm_to_false()
            # await = 6 day 23 hours and 30 min
            await_time = (60 * 60 * 24 * 7) - (60 * 30)

        await asyncio.sleep(await_time)


async def check_lost_pray(bot: Bot, await_time: int = 60) -> None:
    """
    :param bot: bot
    :param await_time: time in seconds for awaiting
    """
    while True:
        time_now = timedelta(
            hours=datetime.now().hour,
            minutes=datetime.now().minute
        )
        week_day_now = datetime.weekday(datetime.now())

        if (timedelta(hours=9, minutes=0) < time_now) and week_day_now == 5:
            story: list[Story] = get_reports_false_pray_last_week()
            users = Counter()
            for lost_day in story:
                users[lost_day.chat_id] += 1
            for chat_id, lost_day in users.most_common():
                if lost_day < 2:
                    continue
                elif lost_day > 2:
                    text = f'За последние 7 дней ты пропустил {lost_day} раз молитву\n' \
                           f'о пропуска будет сообщено лидеру'
                    await bot.send_message(241097915, f'{chat_id} не молился')
                else:
                    text = f'За последние 7 дней ты пропустил {lost_day} раз молитву'
                await bot.send_message(chat_id, text)

            # await = 23 hours and 55 min
            await_time = (60 * 60 * 24) - (60 * 5)

        await asyncio.sleep(await_time)
