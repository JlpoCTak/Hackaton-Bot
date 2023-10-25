import time
import logging

from aiogram import types, F, Router
from aiogram.handlers import message
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup, InlineKeyboardButton
import aiogram.filters.callback_data as filters
from aiogram.contrib.fsm_storage.memory import MemoryStorage # Для проф бота
from aiogram.utils.markdown import hbold
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import State, StatesGroup
import json
from kb import keyboard1, keyboard2


# from kb import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
# import text

# from prof_test import test_holland
router = Router()

storage = MemoryStorage()
logging.basicConfig(level= logging.INFO)
db = Database('database.db')

class RegisterFSM(StatesGroup):
    nickname_input = State()
    pass_input = State()
@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(
        f"'Првиет, {msg.from_user.full_name}, я бот'",
        reply_markup=keyboard1)

@router.message(Command("Logging"))
async def Logging_or_register(msg: types.Message):
    await msg.answer("Хотите-ли ")