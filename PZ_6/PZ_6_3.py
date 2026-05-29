#Дан список размера N и целое число K (1 < K < N). Осуществить сдвиг элементов
#списка вправо на K позиций (при этом A1 перейдет в AK+1, A2 — в AK+2, ..AN-K — в
#AN, а исходное значение K последних элементов будет потеряно). Первые K
#элементов полученного списка положить равными 0.
import random

a = []
for i in range(10):
    random_int = random.randint(1, 100)
    a.append(random_int)


def my_list(lst, k):
    n = len(lst)

    res = [0] * k + lst[:n - k]
    return res

print('Список', a)
print('Список со сдвигом',my_list(a,3))