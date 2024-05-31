import asyncio
from datetime import date, datetime, timedelta
from collections import Counter

from aiogram import Bot

from db.plna_db_handl import get_immediate_plans, update_all_total_alarm_to_false, delete_plan_by_id, \
    delete_plan_by_type
from db.story_db_handl import add_report_pray, get_reports_lost_pray_last_week
from db.user_db_handl import get_users, get_user_by_chat_id
from bot.utils.send_message import prayer_reminder
from bot.keyboards.inline_keyboards.is_pray import is_pray_markup


async def check_reminders(bot: Bot, await_time: int = 60) -> None:
    """
    :param bot: bot
    :param await_time: time in seconds for awaiting
    """
    while True:
        plans = get_immediate_plans()
        for plan in plans:
            if get_user_by_chat_id(plan.chat_id).is_reminders:
                await prayer_reminder(plan.chat_id, bot, plan.time, plan.id)

        await asyncio.sleep(await_time)


async def check_pray(bot: Bot) -> None:
    """
    :param bot: bot
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

        await_time = 60 * 15
        if timedelta(hours=8, minutes=00) < time_now < timedelta(hours=8, minutes=20):

            yesterday = date.today() - timedelta(days=1)
            yesterday_date = yesterday.strftime("%d ")
            yesterday_date += months[yesterday.strftime("%m")]
            users = get_users()

            for user in users:
                add_report_pray(user.chat_id, False, yesterday)
                await bot.send_message(
                    user.chat_id,
                    f'Помолился ли ты {yesterday_date}?',
                    reply_markup=is_pray_markup(yesterday.strftime('%d %m %Y'))
                )

            await_time = 60 * 60 * 23

        await asyncio.sleep(await_time)


async def restart_reminder_status() -> None:
    """
    param await_time: time in seconds for awaiting
    """
    while True:
        time_now = timedelta(
            hours=datetime.now().hour,
            minutes=datetime.now().minute
        )
        week_day_now = datetime.weekday(datetime.now())

        await_time = 60 * 15
        if (timedelta(hours=0, minutes=00) < time_now < timedelta(hours=1, minutes=00)) and week_day_now == 0:

            delete_plan_by_type("postponement")
            update_all_total_alarm_to_false()

            await_time = 60 * 60 * 24 * 6

        await asyncio.sleep(await_time)


async def check_lost_pray(bot: Bot) -> None:
    """
    :param bot: bot
    """
    while True:
        time_now = timedelta(
            hours=datetime.now().hour,
            minutes=datetime.now().minute
        )

        await_time = 60 * 15

        if timedelta(hours=19, minutes=00) < time_now < timedelta(hours=19, minutes=30):
            story = get_reports_lost_pray_last_week()
            users = Counter()
            for lost_day in story:
                users[lost_day.chat_id] += 1
            for chat_id, lost_day in users.most_common():
                if lost_day < 2:
                    continue
                elif lost_day > 2:
                    text = f'За последние 7 дней ты пропустил {lost_day} раз молитву\n' \
                           f'о пропуска будет сообщено лидеру'

                    user = get_user_by_chat_id(chat_id)
                    name = ("@" + user.user_name) if user.user_name is not None else user.first_name
                    lider_chat = 241097915 if user.lieder is None else user.lieder
                    await bot.send_message(lider_chat, f'{name} не молился {lost_day} раз')
                else:
                    text = f'За последние 7 дней ты пропустил {lost_day} раз молитву'
                await bot.send_message(chat_id, text)

            await_time = 60 * 60 * 23

        await asyncio.sleep(await_time)
