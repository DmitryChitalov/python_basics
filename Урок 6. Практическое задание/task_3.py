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
    name = ''
    surname = ''
    position = None
    _income = {'wage': 0, 'bonus': 0}

    def __init__(self, income):
        self._income = income

    def __str__(self):
        total_income = 0
        for key in self._income:
            total_income += self._income.get(key)        
        return f'Worker: {self.position} {self.name} {self.surname}.\n Income = {total_income}'
        

class Position(Worker):

    def get_full_name(self):       
        print(f'Worker full name: {self.name} {self.surname}')

    def get_total_income(self):
        total_income = 0
        for key in self._income:
            total_income += self._income.get(key)
        print(f' Income = {total_income}')
        return total_income
    
        
income_dict = {'wage': 100000, 'bonus': 500}
new_worker = Worker(income_dict)
new_worker.position = 'manager'
new_worker.name = 'Sasha'
new_worker.surname = 'Reddy'
print(new_worker)
new_pos = Position(income_dict)
new_pos.position = 'developer'
new_pos.name = 'Ali'
new_pos.surname = 'Kobano'
print(new_pos)
new_pos.get_full_name()
new_pos.get_total_income()
