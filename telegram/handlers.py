import time
import logging

from aiogram import types, F, Router
from aiogram.handlers import message
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup, InlineKeyboardButton
import aiogram.filters.callback_data as filters
# from aiogram.contrib.fsm_storage.memory import MemoryStorage # Для проф бота
from aiogram.utils.markdown import hbold
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import State, StatesGroup
import json
from kb import keyboard1, keyboard2
import sqlite3


# from kb import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
# import text

# from prof_test import test_holland
router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    connection = sqlite3.connect('database/Users.db')
    cursor = connection.cursor()
    user_id = msg.from_user.id
    user_check = f'''SELECT * FROM Users WHERE Tg user id = {user_id}'''
    if (user_check):
        print(1)

    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Админ-панель",
        callback_data="Test")
    )
    await msg.answer(
        f'Привет,Админ {msg.from_user.full_name}, нажми на кнопку, чтобы вйоти в админ-панель',
        reply_markup=builder.as_markup()
    )
@router.message(Command("Logging"))
async def Logging_or_register(msg: types.Message):
    await msg.answer("Хотите-ли ")