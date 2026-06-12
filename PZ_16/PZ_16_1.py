'''Создайте класс "Животное" с атрибутами "имя" и "вид". Напишите метод, который
выводит информацию о животном в формате "Имя: имя, Вид: вид".
'''

class Animals:
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind

    def output(self):
        print('Имя:', self.name)
        print('Вид:', self.kind)

animal_1 = Animals('Мурка', 'Кошка')
animal_2 = Animals('Рекс', 'Собака')


animal_1.output()
animal_2.output()



        