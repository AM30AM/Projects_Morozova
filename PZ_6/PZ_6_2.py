#Дан список размера N. Найти два соседних элемента, сумма которых максимальна,
#и вывести эти элементы в порядке возрастания их индексов.

def my_list(lst):
    n = len(lst)

    #первая пара
    max_sum = (lst[0]+lst[1])
    res = (lst[0], lst[1])

    for i in range(1, n):
        sum = lst[i-1] + lst[i]
        if sum > max_sum:
            max_sum = sum
            res = lst[i-1], lst[i]

    return res

a = [2, 3, 4, 5, 1]
print('Список: ', a)
print('Максимальная сумма елементов:', my_list(a))
