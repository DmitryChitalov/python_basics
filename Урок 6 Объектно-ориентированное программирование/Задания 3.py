"""Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
атрибутов, вызвать методы экземпляров).
"""


class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        income = self._income['wage'] + (self._income['wage'] * self._income['bonus'])
        return int(income)


worker_1 = Position('Ivan', 'Ivanov', 'ceo', {'wage': 100, 'bonus': 0.1})
w_1 = worker_1.get_total_income()
print(f'{worker_1.get_full_name()} have {w_1}$ hour profit')
worker_2 = Position('Mihail', 'Prohorov', 'managing partner', {'wage': 1500, 'bonus': 0.25})
w_2 = worker_2.get_total_income()
print(f'{worker_2.get_full_name()} have {w_2}$ hour profit')
worker_3 = Position('V', 'B', 'owner', {'wage': 77777, 'bonus': 0.75})
w_3 = worker_3.get_total_income()
print(f'{worker_3.get_full_name()} have {w_3}$ hour profit')

"""
Ivan Ivanov have 110$ hour profit
Mihail Prohorov have 1875$ hour profit
V B have 136109$ hour profit
"""
