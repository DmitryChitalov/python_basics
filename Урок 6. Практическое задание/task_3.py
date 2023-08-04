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
    _income = {}

    def __init__(self, name,surname,position,wage,bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income["wage"] = wage
        self._income["bonus"] = bonus

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'\nПолное имя: {self.name} {self.surname}'

    def get_total_income(self):
        return f'\nСовокупный доход: {sum(self._income.values())} руб.'

    def __str__(self):
        return f'{self.get_full_name()}, {self.get_total_income()}'


first_worker = Position("Василий", "Лемонадов", "Менеджер среднего звена", 120008, 1200)
print(first_worker)

second_worker = Position("Анатолий", "Гогриндинский", "Бариста", 250000, 45000)
print(second_worker)