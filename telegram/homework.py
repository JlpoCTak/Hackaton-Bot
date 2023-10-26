# id den nedel data group prepod predmet ssilka dz
# выбирает день урок и прикрепляет файл для скачивания
#выбирает день урок и если есть прикрепленный файл то имеет возможность скачать его

import sqlite3


def prepod():

    connection = sqlite3.connect('C:\\Users\\Sokol\\Documents\\GitHub\\Hackaton-Bot\\database\\Users.db')
    cursor = connection.cursor()

    # id = input("Введите айди: ")
    weak_day = input("Введите день недели: ")
    data = input("Введите дату: ")
    student_class = input("Введите группу: ")
    teacher = input("Введите учителя: ")
    lesson = input("Введите урок: ")
    href = 'database/homework/dz.docx'

    connection.execute(
        "INSERT INTO homework VALUES (id = ?, weak_day = ?, data = ?, student_class = ?, teacher = ?, lesson = ?, href = ?)",
        (id, weak_day, data, student_class, teacher, lesson, href))

    cursor.execute("INSERT INTO homework VALUES (?, ?, ?, ?, ?, ?)", (weak_day, data, student_class, teacher, lesson, href))

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

    print("Задание не найдено.")

# выбирает день урок и если есть прикрепленный файл то имеет возможность скачать его
# prepod()

    print("По этим урокам в этот день не найдено никакого домашнего задания")

    conn.close()

    print("Задание не найдено.")

# выбирает день урок и если есть прикрепленный файл то имеет возможность скачать его
# prepod()
