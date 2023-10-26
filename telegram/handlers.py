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
import json
from kb import keyboard1, keyboard2
import sqlite3
import os

# from kb import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
# import text
TOKEN = os.environ['TOKEN']
# from prof_test import test_holland
router = Router()
bot = Bot(token=TOKEN,parse_mode=ParseMode.HTML)

class admin_FSM(StatesGroup):
    take_status = State()
    take_menu = State()
    enter_depart = State()

class teacher_FSM(StatesGroup):
    take_status = State()

class student_FSM(StatesGroup):
    take_status = State()

@router.message(Command("start"))
async def start_handler(msg: Message,state:FSMContext):

    connection = sqlite3.connect('database/Users.db')
    cursor = connection.cursor()
    user_id = msg.from_user.id
    user_check_admin = f'''SELECT EXISTS(SELECT Fio FROM Admin WHERE Tg_users_ID = ?)'''

    status = 0
    user_check_teacher = f'''SELECT EXISTS(SELECT Fio FROM Teacher WHERE Tg_users_ID = ?)'''
    user_check_student = f'''SELECT EXISTS(SELECT Fio FROM Student WHERE Tg_users_ID = ?)'''
    check_admin = cursor.execute(user_check_admin, (user_id,))


    for check1 in check_admin:
        if list(check1)[0] == 1:
            status = 'admin'
            await state.set_state(admin_FSM.take_status)
        break
    check_teacher = cursor.execute(user_check_teacher, (user_id,))
    for check2 in check_teacher:
        if list(check2)[0] == 1:
            status = 'teacher'
        break
    check_student = cursor.execute(user_check_student, (user_id,))
    for check3 in check_student:
        if list(check3)[0] == 1:
            status = 'student'
        break

    if status == 'admin':
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(
            text="Админ-панель",
            callback_data="admin_menu")
        )
        await msg.answer(
            f'Привет,Админ {msg.from_user.full_name}, нажми на кнопку, чтобы войти в админ-панель',
            reply_markup=builder.as_markup()
            )
        await state.set_state(admin_FSM.take_menu)

    elif status == 'teacher':
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(
            text="Меню преподавателей",
            callback_data="teacher_menu")
        )
        await msg.answer(
            f'Привет,преподаватель {msg.from_user.full_name}, нажми на кнопку меню',
            reply_markup=builder.as_markup()
        )
    elif status == 'student':
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(
            text="Меню студента",
            callback_data="student_menu")
        )
        await msg.answer(
            f'Привет,студент {msg.from_user.full_name}, нажми на кнопку меню',
            reply_markup=builder.as_markup()
        )

@router.callback_query(F.data == 'admin_menu')
async def admin_menu(callback: types.CallbackQuery,state: FSMContext):
    builder = ReplyKeyboardBuilder()
    builder.row(
        types.KeyboardButton(text='Административные отделения', callback_data='administrative_department'),
        types.KeyboardButton(text='Кнопка 2',callback_data=None)
    )
    await callback.message.answer(text='Выберите действие:',reply_markup=builder.as_markup(resize_keyboard=True))
    await state.set_state(admin_FSM.enter_depart)


@router.callback_query(F.data == 'teacher_menu')
async def admin_menu(callback: types.CallbackQuery):
    builder = ReplyKeyboardBuilder()
    builder.row(
        types.KeyboardButton(text='Уч. материалы и д/з', callback_data=None),
        types.KeyboardButton(text='Кнопка 2',callback_data=None)
    )
    await callback.message.answer(text='Выберите действие:',reply_markup=builder.as_markup(resize_keyboard=True))

@router.callback_query(F.data == 'student_menu')
async def admin_menu(callback: types.CallbackQuery):
    builder = ReplyKeyboardBuilder()
    builder.row(
        types.KeyboardButton(text='Уч. материалы и д/з', callback_data=None),
        types.KeyboardButton(text='Расписание',callback_data=None)
    )
    await callback.message.answer(text='Выберите действие:',reply_markup=builder.as_markup(resize_keyboard=True))

class Loggin(StatesGroup):
    admin_name = State()
    admin_email = State()
    admin_department_mode = State()
@router.message(admin_FSM.enter_depart,F.text =='Административные отделения')
async def admin_administrative_depart(msg: Message, state: FSMContext):
    connection = sqlite3.connect('database/Users.db')
    cursor = connection.cursor()
    administrative_departament = f'''SELECT name FROM administrative_department'''
    # name = msg.text
    # print(name)
    check_administrative_departament = cursor.execute(administrative_departament)
    # print(list(check_administrative_departament))
    builder = InlineKeyboardBuilder()

    for name in list(check_administrative_departament):
        builder.add(types.InlineKeyboardButton(
            text=f"{name[0]}",
            callback_data=f"menu_{name[0]}")
        )

    await msg.answer(
        f'Выберите отделение от имени которого хотите войти',
        reply_markup=builder.as_markup()
    )





@router.callback_query(F.data.startswith('menu_'))
async def advertisement_department(callback: types.CallbackQuery):
    connection = sqlite3.connect('database/Users.db')
    cursor = connection.cursor()
    administrative_departament = f'''SELECT name FROM administrative_department'''
    check_administrative_departament = cursor.execute(administrative_departament)
    list_id_student = []
    list_id_teacher = []
    list_id_admin = []

    user_id_student = cursor.execute(f'''SELECT Tg_users_ID FROM Student''')
    for user in user_id_student:
        list_id_student.append(user[0])
    user_id_teacher = cursor.execute(f'''SELECT Tg_users_ID FROM Teacher''')
    for user in user_id_teacher:
        list_id_teacher.append(user[0])
    user_id_admin = cursor.execute(f'''SELECT Tg_users_ID FROM Admin''')
    for user in user_id_admin:
        list_id_admin.append(user[0])


    list_id_all = list_id_student+list_id_teacher+list_id_admin
    name_department = callback.data.split('_')[1]
    await callback.message.answer(text='Напишите ваше сообщение')

    @router.message(admin_FSM.enter_depart)
    async def push_message(msg: Message):
        text_push = msg.text
        for user_id in list_id_all:
            await bot.send_message(chat_id=user_id, text=f'От {name_department}:{text_push}')




