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
    """Car"""

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        """go"""
        print("Машина поехала")

    def stop(self):
        """stop"""
        print("Машина остановилась")

    def turn(self, direction):
        """turn"""
        print(f"Машина повернула {direction}")

    def show_speed(self):
        """show speed"""
        print(f"Текущая скорость {self.speed}")


class TownCar(Car):
    """Town Car"""

    def show_speed(self):
        if self.speed > 60:
            print(f"Скорость превышена. Текущая скорость {self.speed}.")
        else:
            print(f"Текущая скорость {self.speed}")


class SportCar(Car):
    """Sport Car"""
    max_speed = 350


class WorkCar(Car):
    """Work car"""

    def show_speed(self):
        if self.speed > 40:
            print(f"Скорость превышена. Текущая скорость {self.speed}.")
        else:
            print(f"Текущая скорость {self.speed}")


class PoliceCar(Car):
    """Police car"""

    def __init__(self, speed, color, name, is_police=True):
        super().__init__(self, speed, color, name)
        self.is_police = is_police


town_car = TownCar(50, "Красный", "Audi")
print(town_car.speed, town_car.color, town_car.name, town_car.is_police)
town_car.show_speed()

work_car = WorkCar(60, "Желтый", "Cat")
print(work_car.is_police)
work_car.show_speed()

police_car = PoliceCar(120, "Синий", "Ford")
print(police_car.is_police)
police_car.go()
police_car.stop()
police_car.turn("налево")

sport_car = SportCar(200, "Красный", "BMW", False)
print(sport_car.max_speed)
