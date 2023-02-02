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
    def __init__(self, name, speed, color, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"Машина {self.name} поехала"

    def stop(self):
        return f"Машина {self.name} остановилась"

    def turn(self, derection):
        return f"{self.name} повернула {derection}"

    def show_speed(self):
        return f"Скорость {self.name} равна {self.speed}"


class TownCar(Car):
    def show_speed(self):
        # def __init__(self, speed, color, name, is_police):
        #     super().__init__(speed, color, name, is_police)
        if self.speed > 60:
            return "Вы превысили скорость"
        else:
            return f"Скорость {self.name} равна {self.speed}"


class SportCar(Car):
    pass


class WorkCar(Car):
    #def __init__(self, speed, color, name, is_police):
        #super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return "Вы превысили скорость"
        else:
            return f"Скорость {self.name} равна {self.speed}"


class PoliceCar(Car):
    pass


town = TownCar('Audi', 90, 'blue', False)
print(f'1:\n{town.go()}\n{town.show_speed()}\n{town.turn("на лево")}\n{town.turn("на право")}\n{town.stop()}')

sport = SportCar('Nissan GT', 130, 'red', False)
print(f'2:\n{sport.go()}\n{sport.show_speed()}\n{sport.turn("на лево")}\n{sport.stop()}')

work = WorkCar('Ford', 60, 'red', False)
print(f'3:\n{work.go()}\n{work.show_speed()}\n{work.turn("на право")}\n{work.stop()}')

police = PoliceCar('Kia', 100, 'yellow', True)
print(f'4:\n{police.go()}\n{police.show_speed()}\n{police.turn("на право")}\n{police.stop()}')