import sqlite3

connection = sqlite3.connect('database/my.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL
)
''')

cursor.execute('INSERT INTO Users (username, email) VALUES (?, ?)', ('1newuser', '1newuser@example.com'))

connection.commit()
connection.close()

# 1 функция для админ панели  в базу записывается режим отделения, контактная информация, название административного отделения
# 2 функция для пользователей берет данные из базы
# C:\Users\Эмиль\OneDrive\Documents\GitHub\Hackaton-Bot