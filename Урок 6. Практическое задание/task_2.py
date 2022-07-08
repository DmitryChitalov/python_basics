"""
Задание 2.

Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
length (длина в метрах), width (ширина в метрах).

Значения данных атрибутов должны передаваться при создании экземпляра класса.

Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
всего дорожного полотна.

Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
Массу и толщину сделать публичными атрибутами.
Проверить работу метода.

Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т
"""


class Road:
    weight_cm = 1
    height = 1

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def weight_calculation(self):
        try:
            weight = int(self.__length * self.__width * self.height * self.weight_cm)
            print(f"Масса: {weight}кг ({weight / 1000})т")
        except BaseException as e:
            print(f"General error: {e}")


my_road = Road(20, 5000)
my_road.weight_cm = 25
my_road.height = 0.05

my_road.weight_calculation()
