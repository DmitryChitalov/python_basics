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

class Worker():

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surename = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus
        self._income = {'wage': self.wage, 'bonus': self.bonus}

class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surename

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')

w1 = Position('Морозов', 'Илья', 'Системный администратор', 63000, 37000)
print('Работник: ', w1.get_full_name())
print('Должность: ', w1.position)
print('Оклад, руб.: ', w1.wage)
print('Премия, руб.: ', w1.bonus)
print('К выплате, руб. ', w1.get_total_income())

