'''В исходном текстовом файле(dates.txt) найти все даты в форматах ДД.ММ.ГГГГ и
ДД/ММ/ГГГГ. Посчитать количество дат в каждом формате. Поместить в новый
текстовый файл все даты февраля в формате ДД/ММ/ГГГГ.'''

import re 

with open('dates.txt', 'r') as file:
    content = file.read()

date1 = r'\b(\d{2})\.(\d{2})\.(\d{4})\b'
date2 = r'\b(\d{2})/(\d{2})\/(\d{4})\b'

find_date1 = re.findall(date1, content)
find_date2 = re.findall(date2, content)

count_date1 = len(find_date1)
count_date2 = len(find_date2)
print('Количество дат формата дд.мм.гггг: ', count_date1)
print('Количество дат формата дд/мм/гггг: ', count_date2)


february_dates = []

for date in find_date1:
    day, month, year = date
    if month == '02':
        february_dates.append(f"{day}/{month}/{year}")


for date in find_date2:
    day, month, year = date
    if month == '02':
        february_dates.append(f'{day}/{month}/{year}')    


with open('february_dates.txt', 'w') as file:
    for date in february_dates:
       file.write(date + '\n')

print('Даты февраля записаны')
