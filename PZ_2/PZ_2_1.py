#Дано двухзанчное число. Найдите сумму и произведение его цифр

try:
    number = int(input('Введите двухзначное число: '))

    first_n = number // 10
    second_n = number % 10

    summa_number = first_n + second_n
    proisv = first_n * second_n

    print('Сумма цифр числа: ', summa_number)
    print('Произведение цифр числа: ', proisv)
except ValueError:
    print('Что-то пошло не так')