import datetime

from aiogram import F, Router
from aiogram.types import CallbackQuery, ReplyKeyboardRemove

from bot.keyboards.inline_keyboards.postponement_pray_keyboard import PostponementPrayCbData, PostponementPrayActions, \
    build_postponement_pray_time_keyboard
from db.plna_db_handl import add_postponement_plan_by_chat_id, get_plan_by_id

router = Router(name=__name__)


@router.callback_query(
    PostponementPrayCbData.filter(F.action == PostponementPrayActions.postponement)
)
async def handel_postponement_pray(call: CallbackQuery, callback_data: PostponementPrayCbData):
    message = 'На сколько минут сдвинуть молитву?'
    await call.message.edit_text(
        text=message,
        reply_markup=build_postponement_pray_time_keyboard(callback_data.chat_id, callback_data.plan_id)
    )


@router.callback_query(
    PostponementPrayCbData.filter(F.action == PostponementPrayActions.time)
)
async def handel_postponement_pray(call: CallbackQuery, callback_data: PostponementPrayCbData):

    time_now = datetime.datetime.now()
    postponement_time = time_now + datetime.timedelta(minutes=callback_data.time)

    message = f'Напоминание сдвинуто на {postponement_time.hour}:{postponement_time.minute}'
    await call.answer(message)
    await call.message.delete()

    add_postponement_plan_by_chat_id(
        chat_id=callback_data.chat_id,
        day=postponement_time.weekday(),
        start_time=datetime.timedelta(hours=postponement_time.hour, minutes=postponement_time.minute)
    )




