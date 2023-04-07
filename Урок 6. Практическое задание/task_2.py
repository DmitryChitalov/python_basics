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
    spec_mass = 25  # масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см
    thickness = 0.05  # толщина полотна по-умолчанию (в метрах)

    def __init__(self, in_length, in_width):
        self._length = in_length
        self._width = in_width

    def asph_mass(self):
        return self._length * self._width * self.spec_mass * self.thickness


inp_length = int(input("Введите длину дороги в метрах: "))
inp_width = int(input("Введите ширину дороги в метрах: "))
obj_road = Road(inp_length, inp_width)
total_mass = obj_road.asph_mass()
print(f"Масса асфальта для покрытия всего дорожного полотна: {total_mass} кг = {total_mass / 1000:.2f} т")

# Доп. усложнение: пользователь может изменить толщину полотна дороги, заданную в классе по-умолчанию
obj_road.thickness = float(input("Введите актуализированную толщину полотна:"))
total_mass = obj_road.asph_mass()
print(f"Масса асфальта для покрытия всего дорожного полотна: {total_mass} кг = {total_mass / 1000:.2f} т")
