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
    """
    Worker
    """

    def __init__(self, name, surname, position, income_wage, income_bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": income_wage, "bonus": income_bonus}

    def get_wage(self):
        """
        return worker wage
        """
        return self._income["wage"]

    def get_bonus(self):
        """
        return worker bonus
        """
        return self._income["bonus"]

    def __str__(self) -> str:
        return f"Worker {{name: {self.name}, surname: {self.surname}, " \
               f"position: {self.position}, wage: {self._income['wage']}, " \
               f"bonus: {self._income['bonus']}}}"


class Position(Worker):
    """
    Position
    """

    def get_full_name(self):
        """
        return full person name
        """
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        """
        return total income for person
        """
        return self.get_wage() + self.get_bonus()


person = Position("Иван", "Иванов", "менеждер", 30000, 10000)
print(person.name)
print(person.surname)
print(person.position)
print(person._income)
print(person.get_bonus())
print(person.get_wage())
print(person.get_full_name())
print(person.get_total_income())
print(person)
