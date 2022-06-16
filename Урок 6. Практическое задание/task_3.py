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
    def __init__(self, na, su, po):
        self.name = na
        self.surname = su
        self.position = po
        self._income = {"wage": 100, "bonus": 500}


class Position(Worker):
    def __init__(self, na, su, po):
        super().__init__(na, su, po)

    def get_full_name(self):
        print(f'full name is {self.name} {self.surname}')

    def get_income(self):
        print(f'income is {self._income}')

a = Position('Mister', 'Dog', 'dirextor')
a.get_full_name()
a.get_income()