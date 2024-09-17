import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Students (
id INTEGER PRIMARY KEY,
studentname TEXT NOT NULL,
day_of_birth TEXT NOT NULL
)
''')

connection.commit()
connection.close()

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

run = 1
while (run):
    name = input("Введите имя:")
    BD = input("Дата рождения (дд/мм/гггг):")
    cursor.execute('INSERT INTO Students (studentname, day_of_birth) VALUES (?, ?)',
                   (name, BD))
    connection.commit()
    tmp = str(input("Добавить ещё студента? (+ если да): "))
    if (tmp != '+'):
        run = 0

connection.close()
