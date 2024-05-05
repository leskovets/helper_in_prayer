from aiogram import Bot, Dispatcher, types
from peewee import *
import asyncio

import asyncio
import datetime

async def wait_until(dt):
    # sleep until the specified datetime
    now = datetime.datetime.now()
    await asyncio.sleep((dt - now).total_seconds())

async def run_at(coro, dt):
    await wait_until(dt)
    return await coro

async def task_to_run():
    print("Задача выполняется...")

# Запуск задачи в 00, 15, 30 и 45 минут каждого часа
now = datetime.datetime.now()
run_at_times = [now.replace(minute=m, second=0) for m in (0, 15, 30, 45)]
tasks = [run_at(task_to_run(), run_at_time) for run_at_time in run_at_times]

# Используем asyncio.gather, чтобы дождаться выполнения всех задач
asyncio.run(asyncio.gather(*tasks))
