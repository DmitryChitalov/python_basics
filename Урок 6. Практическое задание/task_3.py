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
            self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):
    def get_full_name(self):
        return f'{self.surname} {self.name}'
    def get_total_income(self):
        return int(self._income['wage']) + int(self._income['bonus'])

    def __str__(self):
        return f'__str__:\n{self.surname} {self.name} {self.position} {self.get_total_income()}\n'


with open('task3.txt', 'r', encoding='utf-8') as in_file:
    for line in in_file:
        param = line.split()
        fullinfo = Position(name=param[0], surname=param[1], position=param[2], wage=param[3], bonus=param[4])
        print(f'{fullinfo.get_full_name()} - {fullinfo.position}: {fullinfo.get_total_income()}')
        print(fullinfo)
