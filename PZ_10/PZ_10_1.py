#Средствами языка Python сформировать текстовый файл (.txt), содержащий
#последовательность из целых положительных и отрицательных чисел. Сформировать
#новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
#обработку элементов:
#Исходные данные:
#Количество элементов:
#Максимальный элемент:
#Среднее арифметическое элементов первой трети:

num = ['1, 2, 3, 4, 5, -6, -7, -8, -9, -10']
file_input = open('data_1.txt', 'w')
file_input.writelines(num)
file_input.close()

file_read = open('data_1.txt', 'r')
data_file = file_read.read().strip()
file_read.close()

data = []
nums = data_file.split(',')
for num in nums:
    data.append(int(num))
print('Исходные данные', data)

count = len(data)
print('Количество элементов', count)

max_num = max(data)
print('Максимальный элемент', max_num)

third_size = (count + 2)//3
first_third = []
for i in range(third_size):
    first_third.append(data[i])
print('Первая треть', first_third)

summa = 0
for i in first_third:
    summa += i
averge = summa/len(first_third)
print('Среднее значение первой трети', averge)

file_in = open('data_2.txt', 'w', encoding='utf-8')
file_in.write('Исходные данные: ' + data_file + '\n')
file_in.write('Количество элементов: ' + str(count) + '\n')
file_in.write('Максимальный элемент: ' + str(max_num) + '\n')
file_in.write('Среднее значение первой трети: ' + str(averge) + '\n')
file_in.close()



