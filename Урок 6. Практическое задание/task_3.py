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
    def __init__(self, first_name, last_name, position, wage, bonus):
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, first_name, last_name, position, wage, bonus):
        super().__init__(first_name, last_name, position, wage, bonus)

    def fio(self):
        return f'{self.first_name} {self.last_name}'

    def total(self):
        return self.income['wage'] + self.income['bonus']

    def __str__(self):
        return f'Данные сотрудника\n ФИО: {self.first_name} {self.last_name}\n Должность: {self.position}\n Доход: {self.total()}'


w_atr = Position('Василий', 'Павлов', 'программист', 10000, 1000)
print(w_atr)
