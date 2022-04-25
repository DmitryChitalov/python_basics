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
    def __init__(self, name, color, speed, is_police):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = bool(is_police)

    def go(self):
        if self.speed > 0:
            print(f"Машина {self.name} поехала")
        else:
            pass

    def stop(self):
        if self.speed == 0:
            print(f"Машина {self.name} остановилась")
        else:
            pass

    def turn(self, direction):
        self.direction = direction
        print(f"Машина {self.name} повернула {direction}")

    def show_speed(self):
        print(f"Сейчас скорость у {self.name} {self.speed} км/ч")


class TownCar(Car):
    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f"{self.name} - Превышение скорости!")
        else:
            print(f"Сейчас скорость {self.speed}")


class SportCar(Car):
    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)


class WorkCar(Car):
    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f"{self.name} - Превышение скорости!")
        else:
            print(f"Сейчас скорость {self.speed}")


class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)


tc = TownCar("Мерседес", "красный", 65, 0)
sc = SportCar("Формула1", "белый", 100, 0)
wc = WorkCar("Ролс", "черный", 45, 0)
pc = PoliceCar("BMW", "синий", 0, 1)

print(tc.__dict__)
print(sc.__dict__)
print(wc.__dict__)
print(pc.__dict__)

tc.go()
sc.go()
wc.go()
pc.go()

tc.stop()
sc.stop()
wc.stop()
pc.stop()

tc.show_speed()
sc.show_speed()
wc.show_speed()
pc.show_speed()

sc.turn("направо")