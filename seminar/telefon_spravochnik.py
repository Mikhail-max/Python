from easygui import *
import sqlite3

conn = sqlite3.connect("phonebook.db")

cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS phone (
               name TEXT NOT NULL,
               phone1 TEXT,
               phone2 TEXT,
               email TEXT,
               address TEXT,
               city TEXT
)""")
def all():
    cursor.execute("SELECT * FROM phone")
    result = cursor.fetchall()
    title = "Телефонный Справочник"
    button = "Ok"
    # list = {"Имя", "Телефон", "Доп. Телефон", "Почта", "Адрес", "Город"}
    list = {}
    list1 = []
    # list2 = []


    for row in result:
    #     # msgbox(row, title, button )
        # list = list["Имя"].append(row[0]) + list["Телефон"].append(row[1]) + list["Доп. Телефон"].append(row[2]) + list["Почта"].append(row[3]) + list["Адрес"].append(row[4]) + list["Город"].append(row[5])
        list = {"Имя": row[0], "Телефон": row[1], "Доп. Телефон": row[2], "Почта": row[3], "Адрес" : row[4], "Город": row[5]}
        
        for key, value in list.items():
           list1.append("{0}: {1}""\n".format(key,value) )
   
    list1 = "  " + ' '.join(str(x)+' ' for x in list1)
  
    
    msgbox(list1, title, button )
def find_contact_in_phonebook():
    title = "Телефонный Справочник"
    button = "Ok"
    # list = {"Имя", "Телефон", "Доп. Телефон", "Почта", "Адрес", "Город"}
    list = {}
    list1 = []
    find_contact = enterbox('Введите имя контакта, который нужно найти: ', title)
    sql = "SELECT * FROM phone WHERE name=?"
    cursor.execute(sql, [(find_contact)])
    result_find = cursor.fetchall()
    for row in result_find:
    #     # msgbox(row, title, button )
        # list = list["Имя"].append(row[0]) + list["Телефон"].append(row[1]) + list["Доп. Телефон"].append(row[2]) + list["Почта"].append(row[3]) + list["Адрес"].append(row[4]) + list["Город"].append(row[5])
        list = {"Имя": row[0], "Телефон": row[1], "Доп. Телефон": row[2], "Почта": row[3], "Адрес" : row[4], "Город": row[5]}
        
        for key, value in list.items():
           list1.append("{0}: {1}""\n".format(key,value) )
   
    list1 = "  " + ' '.join(str(x)+' ' for x in list1)
  
    
    msgbox(list1, title, button )

    # msg(result_find, title)
def delete_cont():
    title = "Телефонный Справочник"
    delete_cont = enterbox('Введите контакт, который хотите удалить: ', title)
    result_delete_cont = cursor.execute("SELECT name FROM phone WHERE name=?", (delete_cont, )).fetchone()

    if result_delete_cont:
        cursor.execute("DELETE FROM phone WHERE name=?", (delete_cont, )).fetchone()
    # sql = "DELETE FROM phone WHERE name = ? ", (delete_cont, )
    # cursor.execute(sql)
        conn.commit()
    else:
        msgbox('Такого контакта не существует', title)
def new_cont():
    contact = enterbox("Введите имя нового контакта:", title)
    result_contact = cursor.execute("SELECT name FROM phone WHERE name=?", (contact, )).fetchone()

    if result_contact:
        contact = result_contact
        msgbox('Контакт существует!', title)

    else:
        phone1 = enterbox('Введите телефон нового контакта: ', title)
        phone2 = enterbox('Введите дополнительный телефон нового контакта: ', title)
        email = enterbox('Введите почту нового контакта: ', title)
        address = enterbox('Введите адрес нового контакта: ', title)
        city = enterbox('Введите город нового контакта: ', title)
        data = (contact, phone1, phone2, email, address, city)
        cursor.execute("INSERT INTO phone(name, phone1, phone2, email, address, city) VALUES (?,?,?,?,?,?)", data)
        conn.commit()
def redact_cont():
    edit_contact_old = enterbox('Введите имя контакта, который вы хотите отредактировать: ')
    result_contact = cursor.execute("SELECT name FROM phone WHERE name=?", (edit_contact_old, )).fetchone()
    if result_contact:
        edit_contact_new = enterbox('Введите новое имя контакта: ')
        new_contact = """UPDATE phone set name=?, phone1=?, phone2=?, email=?, address=?, city=? where name=?"""
        phone1 = enterbox('Введите телефон контакта: ')
        phone2 = enterbox('Введите дополнительный телефон контакта: ')
        email = enterbox('Введите почту контакта: ')
        address = enterbox('Введите адрес контакта: ')
        city = enterbox('Введите город контакта: ')
        new_data = (edit_contact_new, phone1, phone2, email, address, city, edit_contact_old)
        cursor.execute(new_contact, new_data)
        conn.commit()
    else:
        msgbox('Контакт не существует!', title)

conn.commit()

while True:

    title = "Телефонный справочник"
    choices = ["Посмотреть все контакты", "Добавить новый контакт", "Удалить контакт", "Найти контакт по имени", "Изменить контакт", "Закончить работу"]
    msg = "Выберите команду"
    reply = choicebox(msg, title, choices = choices)

    if reply == 'Посмотреть все контакты':
        
        #   cursor.execute("SELECT * FROM phone")
        # result = cursor.fetchall()
        # title = "Телефонный Справочник"
        # button = "Ok"
        
        # for row in result:
        #     print(row)
        all()

    elif reply == 'Добавить новый контакт':
        new_cont()
    elif reply == 'Удалить контакт':
        delete_cont()
    elif reply == 'Найти контакт по имени':
        find_contact_in_phonebook()
    elif reply == 'Изменить контакт':
        redact_cont()
    elif reply == 'Закончить работу':
        cursor.close()
        conn.close()
        print("Соединение с SQLite закрыто")
        break