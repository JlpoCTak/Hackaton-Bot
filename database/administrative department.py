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

cursor.execute('INSERT INTO Users (username, email) VALUES (?, ?)', ('newuser', 'newuser@example.com'))

def admin_menu():
    a = input()
    print("Меню администратора")
    if (a == 1):
        adding_a_department()
def adding_a_department():
    id = input()
    name = input()
    email = input()
    department_mode = input()
    cursor.execute('INSERT INTO users (id, name, email, department_mode) VALUES (?, ?, ?, ?)', (id, name, email, department_mode))
def student():
    cursor.execute('SELECT * FROM Users')
    users = cursor.fetchall()

    for user in users:
        print(user)
adding_a_department()
connection.commit()
connection.close()

connection.commit()
connection.close()

# 1 функция для админ панели  в базу записывается режим отделения, контактная информация, название административного отделения
# 2 функция для пользователей берет данные из базы