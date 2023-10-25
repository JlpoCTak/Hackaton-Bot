# id den nedel data group prepod predmet ssilka dz

import sqlite3

connection = sqlite3.connect('users.db')
cursor = connection.cursor()



connection.commit()
connection.close()