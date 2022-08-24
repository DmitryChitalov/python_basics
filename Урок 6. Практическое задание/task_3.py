"""
Задание 3.

Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.

Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать публичные методы
получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).

Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).

П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку __str__
__str__(self) - вызывается функциями str, print и format.
Возвращает строковое представление объекта.
"""
class Worker:
    '''Работник'''
    name = ''
    surname = ''
    position = ''
    _income = {
        "wage": 0,
        "bonus": 0
    }

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

class Position(Worker):
    '''должность'''
    def get_full_name(self):
        '''возврат имени и фамилии'''
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        '''возврат зп с учетом бонусов'''
        return self._income['wage'] + self._income['bonus']

    def __str__(self):
        return f'Имя сотрудника на позиции {self.position}: {self.get_full_name()} \n' \
               f'Совокупный доход равняется: {self.get_total_income()}'

guard = Position('Иванов', 'Иван', 'Охранник', {'wage': 5000, 'bonus': 350})
print(
    f'Имя сотрудника на позиции {guard.position}: {guard.get_full_name()} \n'
    f'Совокупный доход равняется: {guard.get_total_income()}'
)
print(guard)
