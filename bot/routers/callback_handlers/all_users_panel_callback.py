from aiogram import F, Router
from aiogram.types import CallbackQuery

from bot.keyboards.inline_keyboards.user_detail_keyboard import build_user_detail_keyboard
from bot.keyboards.inline_keyboards.all_users_panel_keyboard import AllUsersPanelActions, AllUsersPanelCbData, \
    build_all_users_keyboard

router = Router(name=__name__)


@router.callback_query(
    AllUsersPanelCbData.filter(F.action == AllUsersPanelActions.detail)
)
async def handel_all_users_panel_detail(call: CallbackQuery, callback_data: AllUsersPanelCbData):
    message = f'{callback_data.name}: '
    await call.message.edit_text(
        text=message,
        reply_markup=build_user_detail_keyboard(
            page=callback_data.page,
            total_pages=callback_data.total_pages,
            chat_id=callback_data.chat_id,
            name=callback_data.name)
    )


@router.callback_query(
    AllUsersPanelCbData.filter(F.action == AllUsersPanelActions.root)
)
async def handel_all_users_panel_root(call: CallbackQuery, callback_data: AllUsersPanelCbData):
    await call.message.edit_text(
        text=f'Страница {callback_data.page} из {callback_data.total_pages}',
        reply_markup=build_all_users_keyboard(callback_data.page)
    )


@router.callback_query(
    AllUsersPanelCbData.filter(F.action == AllUsersPanelActions.pre_page)
)
async def handel_all_users_panel_pre(call: CallbackQuery, callback_data: AllUsersPanelCbData):
    await call.message.edit_text(
        text=f'Страница {callback_data.page - 1} из {callback_data.total_pages}',
        reply_markup=build_all_users_keyboard(callback_data.page - 1)
    )


@router.callback_query(
    AllUsersPanelCbData.filter(F.action == AllUsersPanelActions.next_page)
)
async def handel_all_users_panel_next(call: CallbackQuery, callback_data: AllUsersPanelCbData):
    await call.message.edit_text(
        text=f'Страница {callback_data.page + 1} из {callback_data.total_pages}',
        reply_markup=build_all_users_keyboard(callback_data.page + 1)
    )
