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
    """
    Вычисления для строительства дороги

    Attributes:
        mass       масса асфальта
        thickness  толщина полотна
        _length    длина дороги в метрах
        _width     ширина дороги в метрах
    """

    mass = 25
    thickness = 0.05

    def __init__(self, **kwargs):
        """
        Принимает именованные параметры

        :param kwargs:
               int length: присваивается атрибуту _length,
               int width: присваивается атрибуту _width
        """
        self._length = kwargs.get('length')
        self._width = kwargs.get('width')

    def count_asphalt(self):
        """
        Выполняет расчет массы асфальта, необходимого для покрытия всего дорожного полотна

        :return: массa асфальта
        """
        try:
            cut = 1000
            weight = self._length * self._width * self.mass * self.thickness
            unit = 'T' if weight > cut else 'kg'
            weight = weight / cut if weight > cut else weight
            return f"{int(weight)} {unit}"
        except TypeError:
            return None


road = Road(length=20, width=5000)
print(road.count_asphalt())
