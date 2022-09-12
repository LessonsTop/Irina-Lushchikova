"""
TODO 1. Очистить и наполнить базу данных данными из класса(данные предоставлены ниже в списках)
TODO 2. Получить данные из БД и записать их в JSON
Доп. подсказки:
1. База данных прилагается и называется bank.db
2. Классы изменять не нужно
3. Основня структура есть
"""

from MegaClass import Account
from db import *


def main():

    sqlConnect.connect()
    sqlConnect.create_tables([AccountDb])

    account1 = Account('Valera', '+7-900-000-00-00', 'valera@mail.com', 100)
    users = AccountDb.create(account=account1.accountName, phone=str(account1.phone), email=account1.email, balance=account1.balance)
    users.save()
    users = users.select()
    for records in users.tuples().iterator():
        print(records)
        for v in records:
            print(v)

import sqlite3
import json

connection = sqlite3.connect('bank.db')
cursor = connection.cursor()

print(cursor.fetchall())

cursor.execute('DELETE FROM AccountDb;')
connection.commit()
print('We have deleted', cursor.rowcount, 'records from the table.')
cursor.execute('SELECT * FROM AccountDb')
print(cursor.fetchall())
cursor.execute('SELECT * FROM AccountDb')
print(cursor.fetchall())
listNames = ["Valera", "Artem", "Kolya", "Petya", "Kostya"]
listNumbers = ["+7-903-800-00-00", "+7-908-222-80-00", "+79000002121", "89003211234", "89077077070"]
listEmail = ["test@test.ru", "artem@gmail.com", "kolya@mail.ru", "petya@yandex.ru", "kostya@rambler.ru"]
listBalance = [1000, 3450, 980, 1250, 398]
for a, b, c, d in zip(listNames, listNumbers, listEmail, listBalance):
    cursor.execute("INSERT INTO AccountDb(account, phone, email, balance) VALUES (?, ?, ?, ?);", (a, b, c, d))
    connection.commit()
cursor.execute('SELECT * FROM AccountDb')
connection.commit()
print(cursor.fetchall())


""" Вторая часть """


listTable = [[listNames[0], listNumbers[0], listEmail[0], listBalance[0]],
[listNames[1], listNumbers[1], listEmail[1], listBalance[1]],
[listNames[2], listNumbers[2], listEmail[2], listBalance[2]],
[listNames[3], listNumbers[3], listEmail[3], listBalance[3]],
[listNames[4], listNumbers[4], listEmail[4], listBalance[4]]
              ]
# print(listTable)

with open('jsonOutput.json', 'w') as file:
    jsonOutput = json.dumps(listTable, indent=4)
    file.write(jsonOutput)
    print(jsonOutput)


if __name__ == '__main__':
    main()


