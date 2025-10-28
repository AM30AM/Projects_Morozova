#Составить функцию, которая выполнит суммирование числового ряда

def sum_num(num):
    summa = 0
    i = 1
    while i <= num:
        summa += i
        i += 1
    return summa
while True:
    try:
        number = int(input("Введите число: "))
        print("Сумма числового ряда:",sum_num(number))
        break
    except ValueError:
        print("erorr")

