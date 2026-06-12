'''Создайте базовый класс "Транспорт" со свойствами "марка", "модель" и "год
выпуска". От этого класса унаследуйте класс "Автомобиль" и добавьте в него
свойство "тип кузова". '''

class Transports:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def output(self):
        print('Марка:', self.brand)
        print('Модель:', self.model)
        print('Год выпуска:', self.year)

class Avto(Transports):
    def __init__(self, brand, model, year, kind):
        super().__init__(brand, model, year)
        self.kind = kind
    
    def output(self):
        super().output()
        print('Тип кузова:', self.kind)


transport_1 = Transports('Porsche', 'GT3 Cayenne', 2024)

avto_1 = Avto('BMW', 'X5', 2020, 'Внедорожник')

transport_1.output()
avto_1.output()


