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
"""


class Worker:
    _wage = 32000
    _bonus = 6400

    def __init__(self):
        self.name = "Мария"
        self.surname = "Иванова"
        self.position = "Специалист"
        self.__income = {"wage": Worker._wage, "bonus": Worker._bonus}


class Position(Worker):
    def get_full_name(self):
        print(f"{self.name} {self.surname}")

    def get_total_income(self, clock, k, bet_h):
        Worker._wage = bet_h * clock
        Worker._bonus = Worker._wage * k
        print(f"Для данной должности при отработанных {clock}ч оклад - {Worker._wage} премия = {Worker._bonus}")


specialist = Position()
specialist.get_full_name()
print(specialist.position)
specialist.get_total_income(120, 0.2, 200)
