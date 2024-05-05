import asyncio
import logging

from db.models import db_init
from plan.plan_handler import check_reminders, check_pray, restart_reminder_status, check_lost_pray
from bot.routers import router as main_router
from bot.bot_init import bot_init


async def main() -> None:
    logging.basicConfig(level=logging.DEBUG)

    db_init()
    bot, dp = await bot_init()

    dp.include_router(main_router)

    check_plan_task = asyncio.create_task(check_reminders(bot))
    check_report_task = asyncio.create_task(check_pray(bot))
    check_lost_pray_pask = asyncio.create_task(check_lost_pray(bot))
    restart_reminders_task = asyncio.create_task(restart_reminder_status())

    try:
        await dp.start_polling(bot)
        await check_plan_task
        await check_report_task
        await check_lost_pray_pask
        await restart_reminders_task
    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    asyncio.run(main())
