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
from typing import Dict


class Worker:
    name = ''
    surname = ''
    position = 'worker'
    _income: dict[str, int] = {'wage': 0, 'bonus': 0}

    def __init__(self, name, surname, wage, bonus):
        self.name = name
        self.surname = surname
        self._income['wage'] = wage
        self._income['bonus'] = bonus

class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']

    def __str__(self):
        return f"{self.name} {self.surname}, оклад: {str(self._income['wage'])} премия: {str(self._income['bonus'])}"


empl = Position("Иван", "Иванов", 10000, 25000)

print("Полное имя работника: ", empl.get_full_name())
print("Общий доход работника: ", empl.get_total_income())
print("Общая информация о работнике: ", empl)

