from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
import sqlite3
from aiogram import Bot, Router, types
from aiogram.filters import Command
from aiogram import F
router=Router()
connection = sqlite3.connect('photos.db')
cursor = connection.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS photos (id INTEGER PRIMARY KEY AUTOINCREMENT, photo_id TEXT)')


connection.commit()
connection.close()
@router.message(Command(commands=['Share']))
async def cmd_start(message: types.Message):
    await message.answer("Отправьте фотографию")
@router.message(F.Photo)
async def save_photo(message: types.Message, state: FSMContext):
    photo_id = save_photo_to_database(message.photo[-1].file_id)
    await state.update_data(photo_id=photo_id)
    await message.answer(f"Фотография сохранена с идентификатором: {photo_id}")

@router.message(Command(commands=["get_photo"]))
async def cmd_get_photo(message: types.Message, state: FSMContext):
    await message.answer("Введите идентификатор фотографии")

@router.message()
async def process_photo_id(message: types.Message, state: FSMContext):
    photo_id = message.text
    photo_file_id = get_photo_from_db(photo_id)
    await bot.send_photo(message.chat.id, photo_file_id)
