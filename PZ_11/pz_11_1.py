#Организовать и вывести последовательность из N случайных целых чисел. Из
#исходной последовательности организовать новую последовательность, содержащую
#положительные числа. Найти их количество.

import random

n = random.randint(5, 20)
print('Количество случайных чисел:', n)

numbers = [random.choice(range(-20, 20)) for _ in range(n) ]
print('Последовательность случайных чисел', numbers)

positive_numbers = [x for x in numbers if x > 0]
print('Только положительные числа последовательности:', positive_numbers)

positive_count = sum([1 for _ in positive_numbers])
print('Количество положительных числе в последовательности:', positive_count)