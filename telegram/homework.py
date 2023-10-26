# id den nedel data group prepod predmet ssilka dz
# выбирает день урок и прикрепляет файл для скачивания
# выбирает день урок и если есть прикрепленный файл то имеет возможность скачать его

import sqlite3

def prepod():
<<<<<<< HEAD
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
    file_path = print()
=======

    connection = sqlite3.connect('C:\\Users\\Sokol\\Documents\\GitHub\\Hackaton-Bot\\database\\Users.db')
    cursor = connection.cursor()
>>>>>>> a5b61dd4cc8e57a0f5df71c1906f5e62b402ada5

    def insert_link(lesson_name, link):
        query = "INSERT INTO homework (lesson_name, file_path) VALUES (?, ?);"
        cursor.execute(query, (lesson_name, link))
        conn.commit()

    while True:
        data1 = input("Введите дату в формате 'дд.мм.гг': ")
        lesson_name = input("Введите название предмета: ")
        for res in cursor.execute("SELECT * FROM Schedule"):
            lesson_name = res[0]
            link = input()
            insert_link()
        print(lesson_name)
        for lesson_name in lesson_name:
            link = input(f"{lesson_name[0]} - Введите ссылку на задание: ")
            insert_link(lesson_name[0], link)
        break

    # cursor.execute("SELECT * FROM Schedule WHERE data = ? and lesson_name = ?", data1, lesson_name1)

    #вводим дату название пары с помощь. sql select *from таблица дата = дата урок = урок через цикл задавать дз

    conn = sqlite3.connect("database/Users.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO homework (weekday, group_name, teacher, lesson_name, data, file_path) VALUES (?, ?, ?, ?, ?, ?)",
                   (weekday, group_name, teacher, lesson_names, data1,  file_path))

    conn.commit()
    conn.close()
    # выбирает день урок и прикрепляет файл для скачивания

prepod()

def student():
<<<<<<< HEAD
    weekday = input("Введите день недели: ")
    lesson_names = input("Введите урок: ")
=======
    connection = sqlite3.connect('Users.db')
    cursor = connection.cursor()


    day = input("Введите день недели: ")
    date = input("Введите дату: ")
    group = input("Введите группу: ")
    teacher = input("Введите имя учителя: ")
    lesson = input("Введите название урока: ")
    file_path = input("Введите домашнее задание: ")
>>>>>>> a5b61dd4cc8e57a0f5df71c1906f5e62b402ada5

    conn = sqlite3.connect("database/Users.db")
    cursor = conn.cursor()

    cursor.execute("SELECT file_path FROM homework WHERE weekday = ? AND lesson_name = ?", (weekday, lesson_names))
    result = cursor.fetchone()

    if result:
        print("Дамашнее задание можно скачать здесь:", result[0])
    else:

<<<<<<< HEAD
        print("По этим урокам в этот день не найдено никакого домашнего задания")

    conn.close()
    student()
# выбирает день урок и если есть прикрепленный файл то имеет возможность скачать его
=======

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
>>>>>>> a5b61dd4cc8e57a0f5df71c1906f5e62b402ada5
