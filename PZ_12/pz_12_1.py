#В матрице найти сумму и произведение элементов столбца N (N задать с
#клавиатуры).

import random
from functools import reduce

size = int(input("Введите размер матрицы: "))


matrix = [[random.randint(-20, 20) for _ in range(size)] for _ in range(size)]

print("Матрица:")
for row in matrix:
    print(row)


n = int(input("Введите столбец: "))

colum = [x [n-1] for x in matrix]

colum_sum = sum(colum)

colum_mat = reduce(lambda x, y: x * y, colum)

print('Сумма элементов столбца равна', colum_sum)
print('Произвадение элементов столбца:', colum_mat)

