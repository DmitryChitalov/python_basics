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

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.osition = position
        self._income = {'wage': 1500, 'bonus': 200}


class Position(Worker):

    def __int__(self, name, surname, position):
        super().__init__(name, surname, position)

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return int(self._income['wage']) + int(self._income['bonus'])

    def __str__(self):
        return self.get_full_name() + " income " + str(self.get_total_income())


empl = Position("Ivan", "Ivanov", "Ingener")
print(empl.get_full_name())
print(empl.get_total_income())
print(empl)
