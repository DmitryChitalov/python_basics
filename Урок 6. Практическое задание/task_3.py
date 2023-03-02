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
        self.s_name = surname
        self.pos = position
        self._income = int(wage) + int(bonus)

class Position(Worker):
    def __int__(self, name, surname, position, _income):
        super().__int__(name, surname, position, _income)

    def get_full_name(self):
        return f'{self.name} {self.s_name}'

    def get_total_income(self):
        return self._income

    def __str__(self):
        return f'{self.pos} {self.name} {self.s_name} с доходом: {self.get_total_income()} рублей'

l_obj = Position('Алёна', 'Востроухова', "бухгалтер", 58750, 11000)
print(l_obj.get_full_name(), l_obj.get_total_income())
print(l_obj)