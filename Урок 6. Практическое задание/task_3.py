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

    def __init__(self, name, surname, wage, bonus):
        self.name = name
        self.surname = surname
        self._income = {'wage': wage, 'bonus': bonus}

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return sum(self._income.values())


class Position(Worker):
    def __init__(self, position_name, name, surname, wage, bonus):
        self.position_name = position_name
        super().__init__(name, surname, wage, bonus)


tmp = Position('Менеджер', 'Андрей', 'Сергеевич', 10000, 1000)
print(tmp.get_full_name(), tmp.get_total_income())
