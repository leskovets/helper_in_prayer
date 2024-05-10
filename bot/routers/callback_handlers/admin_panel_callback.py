from aiogram import Router, F
from aiogram.types import CallbackQuery

from bot.keyboards.inline_keyboards.admin_panel_keyboard import (
    AdminPanelActions,
    AdminPanelCbData,
    build_admin_panel_keyboard,
)
from bot.keyboards.inline_keyboards.all_users_panel_keyboard import build_all_users_keyboard

router = Router(name=__name__)


@router.callback_query(
    AdminPanelCbData.filter(F.action == AdminPanelActions.all_user)
)
async def handel_admin_panel_button_all_users(call: CallbackQuery):
    await call.message.edit_text(
        text='Страница 1',
        reply_markup=build_all_users_keyboard(1)
    )


@router.callback_query(
    AdminPanelCbData.filter(F.action == AdminPanelActions.admins)
)
async def handel_admin_panel_button_admins(call: CallbackQuery):
    await call.answer(
        text='admins in progress',
        cache_time=30
    )


@router.callback_query(
    AdminPanelCbData.filter(F.action == AdminPanelActions.bad_users)
)
async def handel_admin_panel_button_bad_users(call: CallbackQuery):
    await call.answer()


@router.callback_query(
    AdminPanelCbData.filter(F.action == AdminPanelActions.root)
)
async def handel_admin_panel_button_bad_users(call: CallbackQuery):
    await call.message.edit_text(text="Меню администратора:", reply_markup=build_admin_panel_keyboard())
