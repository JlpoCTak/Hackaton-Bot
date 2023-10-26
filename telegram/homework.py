# id den nedel data group prepod predmet ssilka dz
# выбирает день урок и прикрепляет файл для скачивания
#выбирает день урок и если есть прикрепленный файл то имеет возможность скачать его

import sqlite3

def prepod():
    day = input("Введите день недели: ")
    date = input("Введите дату: ")
    group = input("Введите группу: ")
    teacher = input("Введите имя учителя: ")
    lesson = input("Введите название урока: ")
    file_path = input("Введите домашнее задание: ")

    conn = sqlite3.connect("database/Users.db")
    cursor = conn.cursor()

    # Use a parameterized query
    cursor.execute("INSERT INTO homework (day, date, group_name, teacher, lesson, file_path) VALUES (?, ?, ?, ?, ?, ?)",
                   (day, date, group, teacher, lesson, file_path))

    conn.commit()
    conn.close()

def student():
    day = input("Введите день недели: ")
    lesson = input("Введите урон: ")

    conn = sqlite3.connect("database/Users.db")
    cursor = conn.cursor()

    # Use a parameterized query
    cursor.execute("SELECT file_path FROM homework WHERE day = ? AND lesson = ?", (day, lesson))
    result = cursor.fetchone()

    if result:
        print("Дамашнее задание можно скачать здесь:", result[0])
    else:
        print("По этим урокам в этот день не найдено никакого домашнего задания")

    conn.close()
student()