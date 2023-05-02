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
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position


class Position(Worker):

    def __init__(self, worker, income):
        self.__income = income
        self.name = worker.title
        self.surname = worker.surname
        self.position = worker.position

    def get_full_name(self):
        full_name = self.name + " " + self.surname
        return full_name

    def get_total_income(self):
        self_wage = self.__income['wage']
        total_income = self.__income['wage'] + self.__income['bonus']
        print(f'\nЗаработанная плата сотрудника {self.get_full_name()} составляет {self_wage} руб., а с учетом '
              f'премии {total_income} руб.')


worker_a = Worker('Иван', 'Иванов', 'Тракторист')
position_a = Position(worker_a, {'wage': 60000, 'bonus': 30000})
print(f'\nПолное имя сотрудника: {position_a.get_full_name()}')
position_a.get_total_income()
