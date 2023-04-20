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
    _income = dict(wage=5000, bonus=2000)
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
class Position(Worker):
    def get_full_name(self):
        print(f"полное имея сотрудника: {self.surname +' ' + self.name} ")
    def get_total_income(self):
        print(f"доход с учетом премии: {self._income['wage'] + self._income['bonus']}")

    def __str__(self):
        result = "полное имея сотрудника: " + str(self.surname) + " " + str(
            self.name) + " доход с учетом премии: " + str(self._income['wage'] + self._income['bonus'])
        return result

person = Position("Ivanov", "Peter", "ceo")
person.get_full_name()
person.get_total_income()
print()
print(person.__str__())