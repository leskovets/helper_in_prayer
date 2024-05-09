from datetime import date

from aiogram import Router, F
from aiogram.types import CallbackQuery

from db.story_db_handl import update_report_pray

router = Router(name=__name__)


@router.callback_query(F.data.startswith('edit_user_'))
async def edit(call: CallbackQuery):
    is_pray = True if 'True' in call.data else False
    str_date = call.data.split('_')[3]
    date_pray = date(
        day=int(str_date.split()[0]),
        month=int(str_date.split()[1]),
        year=int(str_date.split()[2])
    )
    update_report_pray(call.message.chat.id, is_pray, date_pray)
    await call.message.delete()
