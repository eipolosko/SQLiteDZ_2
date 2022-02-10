import sqlite3

conn = sqlite3.connect('table.db')
cursor = conn.cursor()
print('Зполните данные о книгах,0-выход из ввода')
while(1):
    titl=input('Введите название книги   ')
    if titl=='0':
        break
    autho=input('Введите автора   ')
    pric=float(input('Введите стоимость   '))
    amoun=int(input('Введите количество проданных книг '))
    cursor.execute('''CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY AUTOINCREMENT, title varchar(50),author varchar(30),price decimal(8,2),amount int) ''')
    cursor.execute('''INSERT INTO book(title,author,price,amount) VALUES (?,?,?,?)''', (titl, autho,pric,amoun))
    cursor.execute('''SELECT*FROM book''')
    k = cursor.fetchall()
print('Список всех книг')
for i in k:
   print(*i)