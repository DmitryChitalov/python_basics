"""
Задание 4.

Реализуйте базовый класс Car. У данного класса должны быть следующие публичные атрибуты:
speed, color, name, is_police (булево).

А также публичные методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).

Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.

Добавьте в базовый класс публичный метод show_speed,
который должен показывать текущую скорость автомобиля.

Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""

class Car:
    """
    Хранит данные о автомобиле и возвращает его действия

    Attributes:
        speed       скорость авто
        is_police   реакция полиции (булево)
        name        марка авто
        color       цвет авто
    """
    speed = 0
    is_police = False

    def __init__(self, **kwargs):
        """
        Принимает именованные параметры

        :param kwargs:
                str name: присваивается атрибуту name,
                str color: присваивается атрибуту color
        """
        self.name = kwargs.get('name')
        self.color = kwargs.get('color')

    def go(self):
        """
        :return: 'машина поехала'
        """
        return 'машина поехала'

    def stop(self):
        """
        :return: 'машина остановилась'
        """
        return 'машина остановилась'

    def turn(self, direction):
        """
        :param str direction: направление поворота  'налево' | 'направо'
        :return: 'машина повернула налево | направо'
        """
        if direction in ('налево', 'направо'):
            return f"машина повернула {direction}"

    def show_speed(self):
        """
        :return: 'скорость авто km/h'
        """
        return f"{self.speed} km/h"


class TownCar(Car):
    """
    переопределяет метод show_speed
    """

    def show_speed(self):
        """
        Возвращает 'превышение скорости' если скорость больше 60
        :return: 'превышение скорости' | 'скорость авто km/h'
        """
        if self.speed > 60:
            return 'превышение скорости'
        else:
            return f"{self.speed} km/h"


class SportCar(Car):
    pass


class WorkCar(Car):
    """
    Возвращает 'превышение скорости' если скорость больше 40
    :return: 'превышение скорости' | 'скорость авто km/h'
    """
    def show_speed(self):
        if self.speed > 40:
            return 'превышение скорости'
        else:
            return f"{self.speed} km/h"


class PoliceCar(Car):
    pass


townCar = TownCar(name='audi', color='красный')
workCar = WorkCar(name='volvo', color='зелёный')

townCar.speed = 65
townCar.is_police = True

workCar.speed = 35
workCar.is_police = False

if townCar.is_police:
    print(f"{townCar.show_speed()}! {townCar.color} {townCar.name}! {townCar.turn('направо')}!")

print(f"{workCar.go()} {workCar.show_speed()}, это {workCar.color} {workCar.name}")