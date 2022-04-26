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
    name = None
    surname = None
    position = None
    profit = None
    bonus = None

    def __init__(self, name, surname, positions, profit, bonus):
        self.name = name
        self.surname = surname
        self.position = positions
        self.profit = profit
        self.bonus = bonus


class Position(Worker):
    def __init__(self, name, surname, positions, profit, bonus):
        super().__init__(name, surname, positions, profit, bonus)
        self.__income = {'Profit is': self.profit, 'Bonus is': self.bonus}

    def get_full_name(self):
        return self.name + self.surname

    def get_full_profit(self):
        return self.__income

manager = Position('Mick', 'John', 'Petr' 'Manager', 500, 1000)


print(manager.get_full_name())
print(manager.get_full_profit())
