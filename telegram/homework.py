# id den nedel data group prepod predmet ssilka dz

import sqlite3

def prepod():
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    
    add_tusk()

    def add_tusk():
        day = input("Введите день недели: ")
        lesson = input("Введите урок: ")
        homework = input("Введите задание: ")

        connection.execute("INSERT INTO homework VALUES (?, ?, ?)", (day, lesson, homework))
        connection.commit()
        print("Задание добавлено успешно!")


    connection.commit()
    connection.close()
    # выбирает день урок и прикрепляет файл для скачивания
def student():
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM homework')

    connection.close()
#выбирает день урок и если есть прикрепленный файл то имеет возможность скачать его