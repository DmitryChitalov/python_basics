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
        self.position = position
        self._income = {"wage": 252525, "bonus": 131313}

class Position(Worker):

    def get_full_name(self):
        print(f"Name: {self.name} {self.surname} ")

    def get_total_income(self):
        print(f"Income: {sum(self._income.values())}")

    def __str__(self):
        full_name = (self.name + ' ' + self.surname)
        and_income = sum(self._income.values())
        x = ("Name: " + full_name + ", income: " + str(and_income))
        return x


person = Position("Linus", "Torvalds", "engeneer")
person.get_full_name()
person.get_total_income()
print(person.__str__())