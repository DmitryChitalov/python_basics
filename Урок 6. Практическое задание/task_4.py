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

import random
from typing import List

class Car:
    """
        Машина
    """
    name = None
    """
        Марка
    """
    color = None
    """
        Цвет
    """
    speed = 0
    """
        Текущая скорость
    """
    is_police = False
    """
        Принадлежность полиции
    """

    _allowed_speed = 60
    """
        Разрешённая скорость
    """

    __correct_directions = {"left", "right", "reverse"}
    """
        Возможные направления изменения движения
    """

    def __init__(self, name, color, is_police) -> None:
        """
            Машина
            :param str name: Марка
            :param str color: Цвет
            :param bool is_bolice: Принадлежность полиции
            :raises ValueError: if arguments have incorrect type
        """
        if type(name) is str and type(color) is str and type(is_police) is bool:
            self.name = name
            self.color = color
            self.is_police = is_police
        else:
            raise ValueError("One or more arguments have incorrect type.")

    def go(self, speed) -> None:
        """
            Начало движения
            :param int speed: Скорость движения
        """
        if type(speed) is int:
            self.speed = speed
        else:
            self.speed = 5
    
        print(f"A car {type(self).__name__} with name {self.name} started going")

    def stop(self) -> None:
        """
            Остановка
        """
        self.speed = 0
        print(f"A car {type(self).__name__} with name {self.name} stopped")

    def turn(self, directon) -> None:
        """
            Поворот в указанном направлении
            :param str direction: Направление поворота
        """
        if list(self.__correct_directions).count(directon) > 0 :
            print(f"A car {type(self).__name__} with name {self.name} turning on {directon}")
        else:
            print(f"Sorry, a car cannot turn on this side ({directon})")

    def show_speed(self) -> None:
        """
            Показ текущей скорости
        """
        print(f"{type(self).__name__} with name {self.name} speed is {self.speed} km/h")



class TownCar(Car):
    """
        Городской автомобиль
    """

    def __init__(self, name, color) -> None:
        """
            Городской автомобиль
            :param str name: Марка
            :param str color: Цвет
        """
        super().__init__(name, color, False)

    def show_speed(self) -> None:
        """
            Показ текущей скорости
        """
        if self.speed > self._allowed_speed:
            print(f"A car {type(self).__name__} with name {self.name} is overspeeding")
        super().show_speed()



class SportCar(Car):
    """
        Спортивный автомобиль
    """

    def __init__(self, name, color) -> None:
        """
            Спортивный автомобиль
            :param str name: Марка
            :param str color: Цвет
        """
        super().__init__(name, color, False)



class WorkCar(Car):

    def __init__(self, name, color) -> None:
        """
            Городской автомобиль
            :param str name: Марка
            :param str color: Цвет
        """
        self._allowed_speed = 40
        super().__init__(name, color, False)

    def show_speed(self) -> None:
        """
            Показ текущей скорости
        """
        if self.speed > self._allowed_speed:
            print(f"A car {type(self).__name__} with name {self.name} is overspeeding")
        super().show_speed()



class PoliceCar(Car):
    """
        Полицейский автомобиль
    """

    def __init__(self, name) -> None:
        """
            Полицейский автомобиль
            :param str name: Марка
        """
        super().__init__(name, "White-blue", True)


cars:List[Car] = [
    TownCar("Toyota", "White"),
    SportCar("Bugatti", "Red"),
    WorkCar("Volkswagen", "White"),
    PoliceCar("Mercedes"),
    TownCar("Lada", "Black"),
    WorkCar("Renault", "White"),
    PoliceCar("Lada")
]

directions = ["left", "right", "reverse", "up", "down"]

for car in cars:
    car.go(random.randint(1, 200))
    car.show_speed()
    car.turn(directions[random.randint(0, len(directions) - 1)])
    car.stop()
    print()