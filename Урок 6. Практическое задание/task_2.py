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
        Дорога
    """
    _length:int = 0
    """
        Длина дороги
    """
    _width:int = 0
    """
        Ширина дороги
    """

    weight_per_square:int = 25
    """
        Вес асфальта на 1 кв. метр на 1 см дорожного покрытия
    """
    height:float = 0.05
    """
        Тодщина дорожного покрытия
    """

    def __init__(self, length:int, width:int) -> None:
        """
            Дорога
            :param int length: Длина дороги
            :param int width: Ширина дороги
        """
        self._length = length
        self._width = width

    def get_road_weight(self) -> float:
        """
            Получение массы асфальта для дорожного покрытия
        """
        return self._length * self._width * self.weight_per_square * self.height


road_1 = Road(5000, 20)
road_2 = Road(10000, 50)
road_3 = Road(5000, 30)

roads = [road_1, road_2, road_3]

road_2.weight_per_square = 30
road_2.height = 0.1

road_3.weight_per_square = 20
road_3.height = 0.15

for i, road in enumerate(roads):
    print(f"Total weight fo road_{i + 1} is {road._length}m * {road._width}m * {road.weight_per_square}kg * {road.height}m = {road.get_road_weight()}kg")