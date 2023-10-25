import sqlite3

connection = sqlite3.connect('database/my.db')
cursor = connection.cursor()

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

# 1 функция для админ панели в базу записывается режим отделения, контактная информация, название административного отделения
# 2 функция для пользователей берет данные из базы
# C:\Users\Эмиль\OneDrive\Documents\GitHub\Hackaton-Bot