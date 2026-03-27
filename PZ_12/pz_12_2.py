#В матрице найти отрицательные элементы, сформировать из них новый массив.
#Вывести размер полученного массива.

import random

size = 3

matrix = [[random.randint(-20, 20) for _ in range(size)] for _ in range(size)]

print("Матрица:")
for row in matrix:
    print(row)

negative_num = [num for row in matrix for num in row if num < 0]

print('Только отицательные числа:', negative_num,'\n','Размер массива:',len(negative_num))

