import sqlite3
from _config import DATABASE_PATH

with sqlite3.connect(DATABASE_PATH) as connection:
    c = connection.cursor()

    c.execute("""CREATE TABLE contacts(name_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL, email TEXT NOT NULL, tnumber INTEGER NOT NULL)""")

    c.execute('INSERT INTO contacts(name, email, tnumber)'
              'VALUES("dima", "chuprin-dmitriy@mail.ru", "89023188689")')

    c.execute('INSERT INTO contacts(name, email, tnumber)'
              'VALUES("olga", "olga-chuprina@mail.ru", "89109891234")')

