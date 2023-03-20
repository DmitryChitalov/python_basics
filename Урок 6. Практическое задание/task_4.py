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
    direction_tmp = ("право", "лево")

    def __init__(self, speed, color, name, is_police=bool(0)):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        if direction in self.direction_tmp:
            print(f"Машина повернула на {direction}")
        else:
            print(f"Нет такого направления {direction}")

    def __str__(self):
        tempo = "полиция" if self.is_police else "не полиция"
        return tempo

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"Ваша скорость {self.speed}, вы привысили скорость")
        else:
            print(f"Ваша скорость {self.speed}")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Ваша скорость {self.speed}, вы привысили скорость")
        else:
            print(f"Ваша скорость {self.speed}")


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name, bool(1))


print(PoliceCar(120, "красный", "ваз"))
print(TownCar(120, "красный", "ваз"))
car001 = SportCar(230, "белый", "ford")
car001.show_speed()
car002 = TownCar(65, "синий", "паз")
car002.show_speed()
