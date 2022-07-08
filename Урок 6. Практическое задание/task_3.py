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
        self.wage = wage
        self.bonus = bonus
        self._income = {"wage": self.wage, "bonus": self.bonus}

    def __str__(self):
        return f'Полное имя {self.name} {self.surname}, оклад + бонус = {self._income["wage"] + self._income["bonus"]}'


class Position(Worker):
    def get_full_name(self):
        return self.name + self.surname

    def get_total_income(self):
        return self.wage, self.bonus


my_worker = Position('Ivan', 'Ivanov', 'engineer', '10000', '5000')

print(my_worker)
print(f'Полное ФИО {my_worker.get_full_name()}')
print(f'Полная зп {my_worker.get_total_income()}')
print(f'{my_worker.name} {my_worker.surname} '
      f'{my_worker.position}'
      f' {my_worker.wage} {my_worker.bonus}')
