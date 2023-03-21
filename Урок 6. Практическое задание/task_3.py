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
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return f'Доход сотрудника {self.name} {self.surname} за месяц: {self._income.setdefault("wage") + self._income.setdefault("bonus")}'

worker_1 = Position('Максим', 'Морозов', 'Системный администратор', 100000, 50000)
worker_2 = Position('Роман', 'Иванов', 'Директор', 300000, 150000)
worker_3 = Position('Ирина', 'Климова', 'Бухгалтер', 80000, 40000)

print(worker_1.get_total_income())
print(worker_2.get_total_income())
print(worker_3.get_total_income())