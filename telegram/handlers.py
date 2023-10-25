import time

from aiogram import types, F, Router
from aiogram.handlers import message
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder
import aiogram.filters.callback_data as filters
from aiogram.utils.markdown import hbold
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import State, StatesGroup
from aiogram.filters.state import State, StatesGroup
import json

from kb import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
import text

# from prof_test import test_holland
router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Кнопка?",
        callback_data="Test")
    )
    await msg.answer(
        f'Првиет, {msg.from_user.full_name}, я бот',
        reply_markup=builder.as_markup()
        )

