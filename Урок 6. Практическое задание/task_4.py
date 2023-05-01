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

    def __init__(self, speed, color, name, is_police):
        try:
            self.speed = speed
            self.color = color
            self.name = name
            self.is_police = bool(is_police)
        except BaseException:
            return "Error. Please, enter data."
            exit(-1)

    def go(self):
        return "Go."

    def stop(self):
        return "Stop."

    def turn_left(self):
        return "Turn left."

    def turn_right(self):
        return "Turn right."

    def show_speed(self):
        print("Machine normal speed.")


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return "Over speed."
        else:
            return "Normal speed"


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return "Over speed."
        else:
            return "Normal speed"


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


vaz = SportCar(100, 'Red', 'vaz', False)
toyta = TownCar(30, 'White', 'toyta', True)
porche = WorkCar(70, 'Rose', 'porche', False)
kia = PoliceCar(110, 'Blue',  'kia', True)


print(vaz.turn_left())
print(toyta.turn_right())
print(porche.stop())
print(kia.go())
print(porche.is_police)
print(kia.is_police)
print(porche.show_speed())
print(kia.show_speed())
