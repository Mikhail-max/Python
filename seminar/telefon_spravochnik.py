import sqlite3
conn = sqlite3.connect("phonebook.db")
# conn.row_factory = sqlite3.Row
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS phone (
               name TEXT NOT NULL,
               phone1 TEXT,
               phone2 TEXT,
               email TEXT,
               address TEXT,
               city TEXT
)""")
# # # Вставляем данные в таблицу
# cursor.execute("""INSERT INTO phone(name, phone1, phone2, email, address, city)
#                   VALUES ('Alex', '89048402617','' , 'alex1975@mail.ru', 'proletarskaya 85', 'Moskva')
#                """
#                )
 
# # # Сохраняем изменения
# conn.commit()
# phone = [('Vika', '89253624565', '89366589674', 'vikentiy21@gmail.com', 'marinovskaya 87', 'Leningrad'),
#          ('Ksenia', '89635825474', '', 'ksyha75@mail.ru', 'ogorodnaya 98', 'Rostov')]

# cursor.executemany("INSERT INTO phone VALUES (?,?,?,?,?,?)", phone)
conn.commit()

while True:
    command = input('Введите команду: ')
    if command == '/all':
        cursor.execute("SELECT * FROM phone")
        result = cursor.fetchall()
        for row in result:
            print(row)
    elif command == '/add.contact':
        contact = input('Введите имя нового контакта: ')
        result_contact = cursor.execute("SELECT name FROM phone WHERE name=?", (contact, )).fetchone()
        if result_contact:
            contact = result_contact
            print('Контакт существует!')
        else:
            phone1 = input('Введите телефон нового контакта: ')
            phone2 = input('Введите дополнительный телефон нового контакта: ')
            email = input('Введите почту нового контакта: ')
            address = input('Введите адрес нового контакта: ')
            city = input('Введите город нового контакта: ')
            data = (contact, phone1, phone2, email, address, city)
            cursor.execute("INSERT INTO phone(name, phone1, phone2, email, address, city) VALUES (?,?,?,?,?,?)", data)
            conn.commit()
    elif command == '/delete.contact':
        delete_cont = input('Введите контакт, который хотите удалить: ')
        result_delete_cont = cursor.execute("SELECT name FROM phone WHERE name=?", (delete_cont, )).fetchone()
        if result_delete_cont:
            cursor.execute("DELETE FROM phone WHERE name=?", (delete_cont, )).fetchone()
        # sql = "DELETE FROM phone WHERE name = ? ", (delete_cont, )
        # cursor.execute(sql)
            conn.commit()
        else:
            print('Такого контакта не существует')
