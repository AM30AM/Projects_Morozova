#Дан список А размера N(N-нечетное число). Вывести его елементы с нечетными номерами
#в порядке убывания номеров: Аn, An-2, An -4, ..., A1. Условный оператор не использовать

import random

a = []
for i in range(10):
    random_int = random.randint(1, 100)
    a.append(random_int)

def my_list(lst):
    new = lst[-1::-2]
    return new

print("Изначальный список", a)
print('Только нечетные номера в прорядке убвания номеров', my_list(a))




