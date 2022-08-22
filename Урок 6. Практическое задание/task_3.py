"""
Задание 3.

Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.

Создать класс Position (должность) на базе класса Worker. В классе Position реализовать публичные
методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
(get_total_income).

Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).

П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку __str__
__str__(self) - вызывается функциями str, print и format. Возвращает строковое представление
объекта.
"""


class Worker:
    """Worker"""

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus
        self._income = {"wage": self.wage, "bonus": self.bonus}

    def __str__(self):
        return f"Имя: {self.name}, Фамилия: {self.surname}, Должность: {self.position}"


class Position(Worker):
    """Position"""

    # def __init__(self, name, surname, position, wage, bonus):
    #     super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        """Get full name"""
        print(f"Полное имя: {self.name} {self.surname}")

    def get_total_income(self):
        """Get total income"""
        print(f"Доход: {self._income['wage'] + self._income['bonus']}")


a = Position("Иван", "Сайкин", "Администратор", 100000, 50000)
print(a)
a.get_full_name()
a.get_total_income()
