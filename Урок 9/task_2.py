"""
Задание 2.

Реализовать метакласс. позволяющий создавать всегда один и тот же объект класса (см. урок)
"""


class MyMeta(type):
    obj = None

    def __call__(cls, *args):
        if cls.obj is None:
            cls.obj = super().__call__(*args)

            return cls.obj
        else:
            return cls.obj


class RoadCalc(metaclass=MyMeta):
    _mass = 25
    _thickness = 0

    def __init__(self, length, width):
        self._length = float(length)
        self._width = float(width)

    def mass_calculation(self):
        result = int(self._length * self._width * self._mass * self._thickness)
        return print(f'Требуемая масса асфальта = {result}(кг) '
                     f'= {int(result / 1000)}(т)')


road1 = RoadCalc(20, 5000)
road2 = RoadCalc(40, 4000)
road3 = RoadCalc(20, 5000)

print(road1 is road2)
print(road1 is road3)
print(road2 is road3)
