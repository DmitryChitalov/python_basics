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

    def __init__(self, length, width):
        self._length = int(length)
        self._width = int(width)
        self.weight_per_one_m = int(25)
        self.height_of_cover = float(0.05)

    def asphalt_weight(self):
        all_cover_weight = self._length * self._width * self.weight_per_one_m * self.height_of_cover
        return all_cover_weight


print(f"Масса асфальта: {Road(20, 5000).asphalt_weight()} кг")
