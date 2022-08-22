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
    name = ""
    surname = ""
    position = ""
    _income = {"wage": 0, "bonus": 0}

    def __str__(self):
        return " ".join(["Worker", self.name, self.surname, self.position])

    def set_income(self, wage=0, bonus=0):
        self._income["wage"] = wage
        self._income["bonus"] = bonus


class Position(Worker):

    def get_full_name(self):
        return " ".join([self.name, self.surname])

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


w1 = Position()
w1.name = "Ivan"
w1.surname = "Ivanov"
w1.position = "Director"
w1.set_income(500, 100)
print(w1)
print(w1.get_full_name())
print(w1.get_total_income())
