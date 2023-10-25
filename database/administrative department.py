import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS administrative_department (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
)
''')

cursor.execute('CREATE INDEX idx_email ON Users (email)')
cursor.execute('INSERT INTO Users (username, email) VALUES (?, ?)', ('newuser', 'newuser@example.com'))

connection.commit()
connection.close()

# 1 функция для админ панели  в базу записывается режим отделения, контактная информация, название административного отделения
# 2 функция для пользователей берет данные из базы