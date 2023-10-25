import sqlite3


# Устанавливаем соединение с базой данных
connection = sqlite3.connect('DataBaseForTeatcher.db')
cursor = connection.cursor()

# Создаем таблицу Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
photoname TEXT NOT NULL,
revense TEXT NOT NULL
)
''')

# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()

@dp.message_handler(content_types=types.ContentType.PHOTO)
async def handle_photo(message: types.Message):
    # Получаем идентификатор фотографии
    photo_id = message.photo[-1].file_id

    # Создаем объект файла
    photo = await bot.get_file(photo_id)

    # Скачиваем файл
    photo_id = message.photo_id
    file = await bot.get_file(photo_id)
    file_path = file.file_path
    await bot.photo.download(file_path,f'database/photos/{photo_id}.jpg')

    # Отправляем пользователю сообщение об успешном сохранении фотографии
    await message.reply('Фотография успешно сохранена!')
