"""
Задание 3.

Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.

Создать класс Position (должность) на базе класса Worker. В классе Position реализовать публичные методы
получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).

Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).

П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку __str__
__str__(self) - вызывается функциями str, print и format. Возвращает строковое представление объекта.
"""


class Worker:
    name: str
    surname: str
    position: str
    _income: dict

    def __init__(self, my_name: str, my_surname: str, my_position: str, my_income: dict):
        self.name = my_name
        self.surname = my_surname
        self.position = my_position
        self._income = my_income


class Position(Worker):

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

    def __str__(self):
        return f"{self.position} {self.get_full_name()} получает {self.get_total_income()} денег."


worker_01 = Position("Иван", "Петров", "Дворник", {"wage": 100, "bonus": 10});

print(f"{worker_01.position} {worker_01.get_full_name()} получает {worker_01.get_total_income()} денег.")
print(worker_01)
