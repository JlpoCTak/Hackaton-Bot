import time
import logging

from aiogram import types, F, Router
from aiogram.handlers import message
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardBuilder
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
    print(msg.from_user.id)
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

    print(status)

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
async def admin_menu(callback: types.CallbackQuery):
    builder = ReplyKeyboardBuilder()
    builder.row(
        types.KeyboardButton(text='Административные отделения', callback_data='administrative_department'),
        types.KeyboardButton(text='Кнопка 2',callback_data=None)
    )
    await callback.message.answer(text='Выберите действие:',reply_markup=builder.as_markup(resize_keyboard=True))


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
@router.message(F.text =='Административные отделения')
async def admin_administrative_depart(msg: Message, state: FSMContext):
    connection = sqlite3.connect('database/Users.db')
    cursor = connection.cursor()
    user_check_administrative_departament = f'''SELECT EXISTS(SELECT name FROM administrative_department WHERE name= ?)'''
    name = message
    print(name)
    check_administrative_departament = cursor.execute(user_check_administrative_departament, (name,))

    await msg.answer(
        text= "Введите название департамента",
    )
    for check1 in check_administrative_departament:
        if list(check1)[0] == 1:
            status1 = 'Вы вошли в департамент'
        break

    print(status1)

    if status1 == 'Вы вошли в департамент':
        await msg.anwer()


