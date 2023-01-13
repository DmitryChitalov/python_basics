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

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        try:
            self._income = {'wage': float(wage), 'bonus': float(bonus)}
        except ValueError:
            raise TypeError(f'Параметры `wage` и `bonus` должны быть типов `float` или `str`')


class Position(Worker):

    def get_full_name(self):
        full_name = self.name + ' ' + self.surname
        return full_name

    def get_total_income(self):
        total_income = self._income.get('wage') * (1 + self._income.get('bonus'))
        return total_income


Manager_1 = Position('Yaroslav', 'Pavlenko', 'Manager', 400, 0.4)
print(f'{Manager_1.get_full_name()} - {round(Manager_1.get_total_income(), 2)}')

Manager_2 = Position('Malvina', 'Pavlenko', 'Manager', 350, 0.35)
print(f'{Manager_2.get_full_name()} - {round(Manager_2.get_total_income(), 2)}')


