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
        self.length = length
        self.width = width
    
    def asphalt_weight(self, thickness, weight_per_square_meter):
        area = self.length * self.width
        return area * thickness * weight_per_square_meter

# Пример использования класса Road
if __name__ == '__main__':
    road = Road(5000, 20)
    thickness = 0.05  # 5 см
    weight_per_square_meter = 25  # 25 кг на 1 кв. м
    asphalt_weight = road.asphalt_weight(thickness, weight_per_square_meter)
    print(f'Для покрытия дороги площадью {road.length} м x {road.width} м, '
          f'толщиной асфальта {thickness} м и массой асфальта {weight_per_square_meter} кг/м2, '
          f'необходимо {asphalt_weight / 1000} тонн асфальта.')
