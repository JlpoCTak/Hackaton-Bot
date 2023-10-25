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