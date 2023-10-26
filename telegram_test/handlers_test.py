import time
import logging
from aiogram import types, F, Router, Bot
from aiogram.handlers import message
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardBuilder
import aiogram.filters.callback_data as filters
# from aiogram.contrib.fsm_storage.memory import MemoryStorage # Для проф бота
from aiogram.utils.markdown import hbold
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import State, StatesGroup
from aiogram.enums import ParseMode
import sqlite3
import os

#from database.Users import Schedule

# from kb import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
# import text

# from prof_test import test_holland
TOKEN = os.environ['TOKEN']
router = Router()
bot = Bot(token=TOKEN,parse_mode=ParseMode.HTML)


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

@router.callback_query(F.data == 'student_menu')
async def admin_menu(callback: types.CallbackQuery):
    builder = ReplyKeyboardBuilder()
    builder.row(
        types.KeyboardButton(text='Уч. материалы и д/з', callback_data=None),
        types.KeyboardButton(text='Расписание',callback_data='Schedule')
    )
    await callback.message.answer(text='Выберите действие:',reply_markup=builder.as_markup(resize_keyboard=True))


@router.callback_query(F.data == 'Schedule')
async def Schedules(callback: types.CallbackQuery):
    connection = sqlite3.connect('database/User.db')
    cursor = connection.cursor()
    connection.execute(f'''Select 
    (id, weekday, student_class, teacher, leasson_name, leasson_number, classroom, data)
     from Schedule Values(?, ?, ?, ?, ?, ?, ?, ?,) ''').fetchall()
    Schedules_list = ['id', 'weekday', 'student_class', 'teacher', 'leasson_name', 'leasson_number', 'classroom', 'data']
    data = Schedules_list
    teacher = Schedules_list
    student_class = Schedules_list
    builder = InlineKeyboardBuilder()
    builder.row(
        types.InlineKeyboardButton(text='Выберите дату', callback_data=None),
        types.InlineKeyboardButton(text='Выберите преподователя', callback_data=None),
        types.InlineKeyboardButton(text='Выберите группу', callback_data=None)
    )
    status = 0
    data_Schedule = f'''SELECT data From Schedule WHERE data = ?'''
    teacher_Schedule = f'''SELECT teacher From Schedule WHERE teacher = ?'''
    student_class_Schedule = f'''SELECT student_class From Schedule WHERE student_class = ?'''

    check_data_Schedule = cursor.execute(data_Schedule, (data,))
    for check1 in check_data_Schedule:
        if list(check1)[0] == 1:
            status = 'Расписание на эту дату есть'
            break
    check_teacher_Schedule = cursor.execute(teacher_Schedule, (teacher,))
    for check2 in check_teacher_Schedule:
        if list(check2)[0] == 1:
            status = 'Расписание для данного преподователя'
            break
    check_student_class_Schedule = cursor.execute(student_class_Schedule, (student_class))
    for check3 in check_student_class_Schedule:
        if list(check3)[0] == 1:
            status = 'Рассписание для данной группы'
            break

    print (status)

    if status == 'Расписание на эту дату есть':
        await callback.message.reply(
            f'Вот расписание на данную дату')


