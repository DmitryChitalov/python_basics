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
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        print(f"{self.surname} {self.name}")

    def get_total_income(self):
        print(f"{float(self._income['wage'] + self._income['bonus'])}")

    def __str__(self):
        print(f"{type(self).__name__}(name={self.name},"
              f" surname={self.surname},"
              f" position={self.position},"
              f" income={self._income})")


my_position = Position("Алексей", "Голубятников", "Инженер", {"wage": 300.00, "bonus": 120.53})
print(my_position.name)
print(my_position.surname)
print(my_position.position)

my_position.get_full_name()
my_position.get_total_income()

my_position.__str__()

