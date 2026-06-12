'''Приложение ТЕЛЕМАСТЕРСКАЯ для автоматизированного контроля работ по
ремонту бытовой техники. БД должна содержать таблицу Ремонт телевизоров, имеющую
следующую структуру записи: Марка телевизора, Завод-изготовитель, Цена, Дата
ремонта, Документ, Мастер, Сумма оплаты'''

import sqlite3 as sq

with sq.connect('tv.db') as con:
    con.execute('PRAGMA foreign_keys = ON')
    cur = con.cursor()

    # Исправленный запрос CREATE TABLE — добавлена запятая после поля price
    cur.execute('''CREATE TABLE IF NOT EXISTS tv_repair(
                id INTEGER PRIMARY KEY,
                brand TEXT NOT NULL,
                manufacturer TEXT NOT NULL,
                price INTEGER NOT NULL,
                date_repair DATE NOT NULL,
                document TEXT NOT NULL,
                master TEXT NOT NULL,
                summa INTEGER NOT NULL)
                ''')

    def add_data():
        """Добавление 10 позиций в БД"""
        sample_data = [
            ('Samsung', 'Южная Корея', 25000, '2023-05-10', 'Акт №123', 'Иванов И.И.', 3500),
            ('LG', 'Южная Корея', 30000, '2023-05-12', 'Акт №124', 'Петров П.П.', 4200),
            ('Sony', 'Япония', 45000, '2023-05-15', 'Акт №125', 'Сидоров С.С.', 5800),
            ('Philips', 'Нидерланды', 28000, '2023-05-18', 'Акт №126', 'Иванов И.И.', 3800),
            ('TCL', 'Китай', 18000, '2023-05-20', 'Акт №127', 'Кузнецов К.К.', 2900),
            ('Xiaomi', 'Китай', 22000, '2023-05-22', 'Акт №128', 'Петров П.П.', 3200),
            ('Hisense', 'Китай', 24000, '2023-05-25', 'Акт №129', 'Сидоров С.С.', 3600),
            ('Panasonic', 'Япония', 38000, '2023-05-28', 'Акт №130', 'Иванов И.И.', 4800),
            ('Sharp', 'Япония', 42000, '2023-06-01', 'Акт №131', 'Кузнецов К.К.', 5200),
            ('Haier', 'Китай', 26000, '2023-06-03', 'Акт №132', 'Петров П.П.', 3400)
        ]

        cur.executemany('''
            INSERT INTO tv_repair (brand, manufacturer, price, date_repair, document, master, summa)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', sample_data)
        con.commit()
        print("10 записей успешно добавлены в базу данных")

#ищем по марке
    def search_brand(brand):
        cur.execute('SELECT * FROM tv_repair WHERE brand = ?', (brand,))
        print('\n Найденные телевизоры по запросу:')
        for row in cur.fetchall():
            print(row)

#ищем по сумме, которая больше указанного занчения
    def search_summa(summa):
        cur.execute('SELECT * FROM tv_repair WHERE summa > ?', (summa,))
        print(f'\n Ремонт с суммой оплаты > {summa}:')
        for row in cur.fetchall():
            print(row)

#ищем по диапозону даты ремота
    def search_date(date_start, date_end):
        cur.execute('SELECT * FROM tv_repair WHERE date_repair BETWEEN ? AND ?', (date_start, date_end,))
        print(f'\n Найденные позиции по дате ремонта с {date_start} по {date_end}:')
        for row in cur.fetchall():
            print(row)

#удаляем данные по id
    def delete_data_id(id):
        cur.execute('DELETE FROM tv_repair WHERE id = ?', (id,))
        con.commit()
        print(f'Удалена запись с id = {id}')

#изменение суммы по докумену
    def edit_data_summa(summa, document):
        cur.execute('''UPDATE tv_repair SET summa = ? WHERE document = ?''', (summa, document,))
        con.commit()
        print(f"Изменена сумма оплаты для {document} на {summa} руб")

    def show_all_data():
        #вывод всех данных из таблицы
        print("\nВСЕ ДАННЫЕ В БАЗЕ")
        cur.execute("SELECT * FROM tv_repair")
        rows = cur.fetchall()
        for row in rows:
            print(row)
