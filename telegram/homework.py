# id den nedel data group prepod predmet ssilka dz
# выбирает день урок и прикрепляет файл для скачивания
# выбирает день урок и если есть прикрепленный файл то имеет возможность скачать его

import sqlite3

def prepod():
    conn = sqlite3.connect("database/Users.db")
    cursor = conn.cursor()
    conn = sqlite3.connect("database/Users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT weekday FROM schedule")
    weekday = cursor.fetchall()
    conn = sqlite3.connect("database/Users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT group_name FROM schedule")
    group_name = cursor.fetchall()
    conn = sqlite3.connect("database/Users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT teacher FROM schedule")
    teacher = cursor.fetchall()
    lesson_name = input("Введите название предмета: ")
    data1 = input("Введите дату: ")
    file_path = input("Введите домашнее задание")

    # print(group_name)
    # print(lesson_name)
    # print(teacher)

    conn = sqlite3.connect("database/Users.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO homework (weekday, group_name, teacher, lesson_name, data, file_path) VALUES (?, ?, ?, ?, ?, ?)",
                   (weekday, group_name, teacher, lesson_name, data1,  file_path))

    cursor.execute("SELECT * FROM Schedule WHERE data = ? and lesson_name = ?", data1, lesson_name)
    conn.commit()
    conn.close()
    # выбирает день урок и прикрепляет файл для скачивания

prepod()

def student():
    weekday = input("Введите день недели: ")
    lesson_name = input("Введите урок: ")

    conn = sqlite3.connect("database/Users.db")
    cursor = conn.cursor()

    cursor.execute("SELECT file_path FROM homework WHERE weekday = ? AND lesson_name = ?", (weekday, lesson_name))
    result = cursor.fetchone()

    if result:
        print("Дамашнее задание можно скачать здесь:", result[0])
    else:

        print("По этим урокам в этот день не найдено никакого домашнего задания")

    conn.close()
    student()
# выбирает день урок и если есть прикрепленный файл то имеет возможность скачать его