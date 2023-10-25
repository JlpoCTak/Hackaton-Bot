# id den nedel data group prepod predmet ssilka dz

import sqlite3

def prepod():
    connection = sqlite3.connect('database/Users.db')
    cursor = connection.cursor()

    id = input("Введите айди: ")
    weak_day = input("Введите день недели: ")
    data = input("Введите дату: ")
    group = input("Введите группу: ")
    teacher = input("Введите учителя: ")
    lesson = input("Введите урок: ")
    href = 'database/homework/dz.docx'

    connection.execute("INSERT INTO homework VALUES (id = ?, weak_day = ?, data = ?, group = ?, teacher = ?, lesson = ?, href = ?)", (id, weak_day, data, group, teacher, lesson, href))
    connection.commit()
    print("Задание добавлено успешно!")

    connection.commit()
    connection.close()
    # выбирает день урок и прикрепляет файл для скачивания
prepod()
def student():
    connection = sqlite3.connect('Users.db')
    cursor = connection.cursor()

    day = input("Введите день недели: ")
    lesson = input("Введите урок: ")

    cursor.execute('SELECT * FROM href')
    connection.execute("SELECT homework FROM href WHERE day=? AND lesson=?", (day, lesson))

    # Вывод задания, если оно найдено
    href = connection.fetchone()
    if href:
        print("Скачать задание:", href[0])
    else:
        print("Задание не найдено.")
    connection.close()
#выбирает день урок и если есть прикрепленный файл то имеет возможность скачать его
# prepod()