import sqlite3

connection = sqlite3.connect('Users.db')
cursor = connection.cursor()

async def connect_to_db('User.db'):
conn = await connect(
id='id',
weekday='weekday',
student_class='student_class',
teacher='teacher',
leasson_name='leasson_name',
leasson_numbe='leasson_number',
classroom='classroom',
data='data'
)
return conn
async def Schedule(id, weekday, student_class, teacher, leasson_name, leasson_number, classroom, data):
    Schedule = cursor.execute("Select all from Schedule Values(?, ?, ?, ?, ?, ?, ?, ?,)", (id, weekday, student_class, teacher, leasson_name, leasson_number, classroom, data)).fetchall

    date = input("Введите дату: ")
    student_class = input("Введите группу: ")
    teacher = input("Введите имя учителя: ")

Schedule()