#  реализовать дескрипторы для любых двух классов

class Car:

    def __init__(self, make, model, engine_volume):
        self.make = make
        self.model = model
        self.engine_volume = engine_volume

    def __str__(self):
        return '{0} model {1} with an engine_volume {2} ltr.'.format(self.make, self.model, self.engine_volume)

car_1 = Car('Chevrolet', 'Lacetti', 1.6)
print(car_1)

class House:

    def __init__(self, name, floor, entrance):
        self.name = name
        self.floor = floor
        self.entrance = entrance
    
    def __str__(self):
        return 'House {0} with {1} floors and {2} entrances has been built this week.'.format(self.name, self.floor, self.entrance)

house_1 = House('Helsinki', 25, 2)
print(house_1)