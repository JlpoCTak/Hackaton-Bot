import asyncio
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
    confirmation_teachers1 = State()
    decision_teacher = State()
    enter_depart = State()

class teacher_FSM(StatesGroup):
    take_status = State()
    take_menu = State()
    take_schedule = State()
    take_groups_lessons = State()
    contact_departments = State()
    download_declaration = State()


class student_FSM(StatesGroup):
    take_status = State()
    take_menu = State()
    take_schedule = State()
    take_teachers_lesson = State()
    contact_departments = State()
    download_materials_hw = State()
    see_curriculum = State()
    see_declaration = State()
    where_take_declaration = State()


@router.message(Command("start"))
async def start_handler(msg: Message, state: FSMContext):

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
        builder.row(types.InlineKeyboardButton(
            text="Админ-панель",
            callback_data="admin_menu")
        )
        builder.row(types.InlineKeyboardButton(
            text="Меню преподавателей",
            callback_data="teacher_menu")
        )
        builder.row(types.InlineKeyboardButton(
            text="Меню студента",
            callback_data="student_menu")
        )
        await msg.answer(
            f'Привет,Админ {msg.from_user.full_name}, нажми на кнопку, чтобы войти в нужное меню',
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
    elif status == 0:
        builder = InlineKeyboardBuilder()
        builder.row(types.InlineKeyboardButton(
            text="Я студент",
            callback_data="student_form")
        )
        builder.row(types.InlineKeyboardButton(
            text="Я преподователь",
            callback_data="confirmation_teacher")
        )
        await msg.answer(f'Привет, выбери ты новичок или студент',reply_markup=builder.as_markup())



    cursor.close()
    connection.commit()
    connection.close()


@router.callback_query(F.data == 'student_form')
async def student_form(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(student_FSM.take_status)
    await callback.message.answer('Введите информацию о себе, разделяя их ";", пишите без ковычек'
                          f'\n(Например:"ФИО;группа;курс")')
    @router.message(student_FSM.take_status)
    async def write_student_db(msg: Message):
        connection = sqlite3.connect('database/Users.db')
        cursor = connection.cursor()
        data_student = list(msg.text.split(';'))
        user_id = msg.from_user.id
        cursor.execute(f'INSERT INTO Student (Fio, Group_stud, Course, Tg_users_ID) VALUES (?, ?, ?, ?)',(data_student[0], data_student[1], data_student[2],user_id))

        builder = ReplyKeyboardBuilder()
        builder.add(
            types.KeyboardButton(text='/start')
        )
        await msg.answer(text='Нажми кнопку старт чтобы начать, как студент',reply_markup=builder.as_markup(resize_keyboard=True))

        cursor.close()
        connection.commit()
        connection.close()


@router.callback_query(F.data == 'confirmation_teacher')
async def student_form(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(teacher_FSM.take_status)
    await callback.message.answer('Введите информацию о себе, разделяя их ";", пишите без ковычек'
                            f'\n(Например:"Фамилия Имя Отчество;Кабинет;группа которой курируете")')

    @router.message(teacher_FSM.take_status)
    async def write_student_db(msg: Message):
        connection = sqlite3.connect('database/Users.db')
        cursor = connection.cursor()
        data_student = list(msg.text.split(';'))
        user_id = msg.from_user.id
        cursor.execute(f'INSERT INTO conformition_teacher (Fio, Classroom, Group_curate, Tg_users_ID) VALUES (?, ?, ?, ?)', (data_student[0], data_student[1], data_student[2],user_id))

        await msg.answer(text='Нам нужно подтвердить, что вы преподователь, ждите, когда вам придет уведомление')

        cursor.close()
        connection.commit()
        connection.close()

@router.callback_query(F.data == 'admin_menu')
async def admin_menu(callback: types.CallbackQuery, state: FSMContext):
    builder = ReplyKeyboardBuilder()
    # builder.row(
    #     types.KeyboardButton(text='Административные отделения', callback='administrative_department'),
    #     types.KeyboardButton(text='Кнопка 2',callback_data=None),
    # )
    builder.row(
        types.KeyboardButton(text='/Меню'),
    )

    await callback.message.answer(text='Войдите в главное меню:',reply_markup=builder.as_markup(resize_keyboard=True))


@router.message(admin_FSM.take_menu,Command('Меню'))
async def return_menu(msg: Message, state: FSMContext):

    builder = ReplyKeyboardBuilder()
    builder.row(
        types.KeyboardButton(text='Административные отделения', callback='administrative_department'),
        types.KeyboardButton(text='Меню расписания', callback_data=None),
    )
    builder.row(
        types.KeyboardButton(text='/Меню пользователей'),
        types.KeyboardButton(text='Подтверждение преподавателей')
    )
    builder.row(
        types.KeyboardButton(text='/start', callback='start'),
    )
    builder.row(
        types.KeyboardButton(text='/Меню'),
    )

    await msg.answer(text='Выберите действие:', reply_markup=builder.as_markup(resize_keyboard=True))
    await state.set_state(admin_FSM.take_menu)


@router.message(admin_FSM.take_menu, F.text=='Меню расписания')
async def schedule_menu(msg: Message):
    builder = ReplyKeyboardBuilder()
    builder.row(
        types.KeyboardButton(text='Скачать расписание'),
        types.KeyboardButton(text='Загрузить расписание'),
    )
    builder.row(
        types.KeyboardButton(text='Уведомить о изменении расписания'),

    )
    builder.row(
        types.KeyboardButton(text='/Меню'),
    )
    await msg.answer(text='У вас появилось Меню расписания',reply_markup=builder.as_markup())


@router.message(admin_FSM.take_menu, F.text == 'Подтверждение преподавателей')
async def confirmation_teacher(msg: Message, state: FSMContext):
    await state.set_state(admin_FSM.confirmation_teachers1)
    connection = sqlite3.connect('database/Users.db')
    cursor = connection.cursor()
    mb_teachers = cursor.execute('SELECT * FROM conformition_teacher')
    list_data_mb_teachers = []
    for mb_teacher in mb_teachers:
        list_data = []
        id1 = mb_teacher[0]
        fio = mb_teacher[1]
        classroom = mb_teacher[2]
        group_curate = mb_teacher[3]
        tg_user_id = mb_teacher[4]
        list_data.append(id1)
        list_data.append(fio)
        list_data.append(classroom)
        list_data.append(group_curate)
        list_data.append(tg_user_id)
        list_data_mb_teachers.append(list_data)

    await msg.answer(text=f'Преподавателей на подтверждение: {len(list_data_mb_teachers)}')
    builder = InlineKeyboardBuilder()
    builder.row(
        types.InlineKeyboardButton(text='Подтвердить',callback_data='confirm_teacher'),
    )
    builder.row(
        types.InlineKeyboardButton(text='Удалить',callback_data='delete_teacher'),
    )
    current_state = str(await state.get_state())



    # if current_state== 'admin_FSM:confirmation_teachers1':
    #     # print('foighfd;kghnfdghfdg')
    for teacher_mb in list_data_mb_teachers:
        proverka= False
        await msg.answer(text=f'ФИО: {teacher_mb[1]}'
                              f'\nКабинет: {teacher_mb[2]}'
                              f'\nКурирует группу: {teacher_mb[3]}',
                         reply_markup=builder.as_markup(resize_keyboard=True))

        @router.callback_query(F.data == 'confirm_teacher')
        async def confirm_teacher(callback: types.CallbackQuery):

            fio = teacher_mb[1]
            classroom = teacher_mb[2]
            group_curate = teacher_mb[3]
            user_id = teacher_mb[4]
            print(fio,classroom,group_curate,user_id)
            global proverka

            proverka=1
            cursor.execute('INSERT INTO Teacher (Fio,Classroom, Group_curate, Tg_users_ID) VALUES (?,?,?,?)',(fio, classroom, group_curate,user_id))
            cursor.execute('DELETE FROM conformition_teacher WHERE Tg_users_ID = ?', (user_id,))

            await callback.message.answer('Преподователь подтвержден')
            await bot.send_message(chat_id=user_id, text='Вы подтверждены, как преподователь!')

            # if F.data == 'confirm_teacher':
            #     proverka = 1


        @router.callback_query(F.data == 'delete_teacher')
        async def delete_teacher(callback: types.CallbackQuery):
            user_id = teacher_mb[4]
            global proverka
            # if user_id == user_id:
            proverka = True
            cursor.execute('DELETE FROM conformition_teacher WHERE Tg_users_ID = ?', (user_id,))
            await callback.message.answer('Преподователь удален')
            await bot.send_message(chat_id=user_id, text='Вы не прошли проверку!')

            # if F.data=='delete_teacher':
            #     proverka = 1

        @router.callback_query(F.data=='delete_teacher' or F.data == 'confirm_teacher')
        async def inc_proverka():
            global proverka
            proverka = True


        if proverka == True:
            continue
        else:
            while proverka==False:
                print('sadsad')
                await asyncio.sleep(1)
                if proverka==True:
                    break




    await state.set_state(admin_FSM.confirmation_teachers1)



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
        types.KeyboardButton(text='Расписание',callback_data='Schedule')
    )
    await callback.message.answer(text='Выберите действие:', reply_markup=builder.as_markup(resize_keyboard=True))




@router.message(admin_FSM.take_menu, F.text =='Административные отделения')
async def admin_administrative_depart(msg: Message, state: FSMContext):
    await state.set_state(admin_FSM.enter_depart)
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

    builder.row(types.InlineKeyboardButton(
        text=f'Cоздать отделение',
        callback_data=f'create_depart'
    ))
    builder.adjust(2)
    await msg.answer(
        f'Выберите отделение от имени которого хотите войти, или создайте новое отделение',
        reply_markup=builder.as_markup()
    )
    cursor.close()
    connection.commit()
    connection.close()

@router.callback_query(F.data == 'create_depart')
async def create_department(callback: types.CallbackQuery):

    await callback.message.answer(f'Напишите данные административного отделения, разделяя их ";", пишите без ковычек'
                                  f'\n(Например:"название отделения;время работы;почта;номер отделения")')

    @router.message(admin_FSM.enter_depart)
    def insert_data_depart(msg: Message):
        connection = sqlite3.connect('database/Users.db')
        cursor = connection.cursor()
        data_list = list(msg.text.split(';'))
        cursor.execute(f'INSERT INTO administrative_department (name,department_mode,email,number) VALUES (?,?,?,?)',(data_list[0],data_list[1],data_list[2],data_list[3],))

        cursor.close()
        connection.commit()
        connection.close()


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
            await bot.send_message(chat_id=user_id, text=f'От {name_department}: {text_push}')

    cursor.close()
    connection.commit()
    connection.close()
