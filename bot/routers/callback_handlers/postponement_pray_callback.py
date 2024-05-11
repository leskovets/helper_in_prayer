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
    message = f'Напоминание сдвинуто на {callback_data.time} минут'
    await call.answer(message)
    await call.message.delete()

    first_plan = get_plan_by_id(callback_data.plan_id)

    add_postponement_plan_by_chat_id(
        chat_id=callback_data.chat_id,
        day=first_plan.day,
        start_time=datetime.timedelta(
            hours=first_plan.time.hour, minutes=first_plan.time.minute
        ) + datetime.timedelta(minutes=callback_data.time)
    )




