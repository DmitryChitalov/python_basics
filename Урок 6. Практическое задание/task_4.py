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


class Worker:
    name = ''
    surname = ''
    position = ''
    _income = {"wage": 500, "bonus": 300}


class Position(Worker):
    def get_full_name(self):
        return str(self)

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']

    def __str__(self):
        return f"{self.name} {self.surname}"


pos = Position()
pos.name = 'Jane'
pos.surname = 'Doe'
pos.position = 'Developer'
print(f"Full name via method: {pos.get_full_name()}")
print(f"Full name via magic: {pos}")
print(f"Total income: {pos.get_total_income()}")
