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
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

        # self.wage = wage_bonus["wage"]
        # self.bonus = wage_bonus["bonus"]

    def __str__(self):
        return self.name + " " + self.surname + " " + self.position


class Position(Worker):

    def get_full_name(self):
        return self.name + self.surname

    def get_total_income(self):
        return int(self._income["wage"]) + int(self._income["bonus"])


income__ = {"wage": 10000, "bonus": 5000}
print(Position("ya", "yu", "mn", income__).get_full_name())
print(Position("ya", "yu", "mn", income__).get_total_income())
print(Position("ya", "yu", "mn", income__)._income)
print(Position("ya", "yu", "mn", income__).position)
print(Position("ya", "yu", "mn", income__))
