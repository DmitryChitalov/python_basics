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
class Vehicle:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def police(self):
        if self.is_police:
            return 'Полицейская машина'
        else:
            return 'Гражданская машина'

    def full_info(self):
        return " {} {} Максимальная скорость {} км/ч ".format(self.color, self.name, str(self.speed))

    def go(self):
        return "Машина поехала"

    def stop(self):
        return"Машина остановилась"

    def turn(self):
        return"Машина повернула"


class TownCar(Vehicle):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class SportCar(Vehicle):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Vehicle):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class PoliceCar(Vehicle):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


t_c = TownCar(160, "Black", "Shkoda", False)
print(t_c.police() + t_c.full_info() + t_c.turn())

s_c = SportCar(250, "Red", "Audi", False)
print(s_c.police() + s_c.full_info() + s_c.go())

w_c = WorkCar(50, "Green", "UAZ", False)
print(w_c.police() + w_c.full_info() + w_c.stop())

p_c = PoliceCar(400, "White", "BMW", True)
print(p_c.police() + p_c.full_info() + p_c.go())