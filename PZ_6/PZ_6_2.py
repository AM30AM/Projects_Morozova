#Дан список размера N. Найти два соседних элемента, сумма которых максимальна,
#и вывести эти элементы в порядке возрастания их индексов.

import random

a = []
for _ in range(10):
    random_int = random.randint(1, 100)
    a.append(random_int)

def my_list(lst):
    n = len(lst)

    #первая пара
    max_sum = (lst[0]+lst[1])
    res = (lst[0], lst[1])

    for i in range(1, n):
        suma = lst[i-1] + lst[i]
        if suma > max_sum:
            max_sum = suma
            res = lst[i-1], lst[i]

    return res

print('Список: ', a)
print('Максимальная сумма елементов:', my_list(a))
