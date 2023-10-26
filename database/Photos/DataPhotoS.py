import sqlite3
#нужен токен и import telebot
import random
# Устанавливаем соединение с базой данных
connection = sqlite3.connect('DataBaseForStudent.db')
cursor = connection.cursor()

# Создаем таблицу Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
photoname TEXT NOT NULL,
img TEXT NOT NULL
)
''')

# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()

 # github(должно работать)
@bot.message_handler(content_types=['document'])
def handle_docs_photo(message):
    bot.send_message(message.chat.id, 'отправь картинку заявления: ')
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    file_name = 'img_' + str(random.randint(1, 10000)) + '.jpg'
    with open(file_name, 'wb') as file:
        file.write(downloaded_file)
        bot.reply_to(message, 'ваше изображение сохранено')
    with open('database/Photos/' + file_name, 'wb') as file:
        file.write(downloaded_file)
flag = False
@bot.message_handler(commands=['text'], func=lambda message: True)
def get_text_1(message):
    global nazvanie, flag
    if not flag:
        bot.send_message(message.chat.id, 'введите название заявления: ')
        nazvanie = message.text
        flag = True
    else:
        bot.send_message(message.chat.id, 'вы уже находитесь в процессе ввода другой информации')

    conn = sqlite3.connect('DataBaseForStudent.db')
    cursor = conn.cursor()
    img = 'img_' + str(random.randint(1, 1000)) + '.jpg'
    data= [nazvanie, cost, img]
    cursor.execute("INSERT INTO katalog VALUES(?, ?);", data)
    conn.commit()

#отправка списка студенту/преподу


con = sqlite3.connect('DataBaseForTeatcher.db')
cur = con.cursor()
cur.execute("""SELECT * FROM revense""")
result = cur.fetchall()

@dp.message_handler()
async def get_profile(message: types.Message):
    for photoname in result:
        await bot.send_message(message.from_user.id, photoname[0])'\n'.join(result)

if __name__ == '__main__':
    executor.start_polling(dp)
