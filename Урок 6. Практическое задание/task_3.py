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
        self.__income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        return f"Полное имя сотрудника: {self.surname} {self.name}"
    def get_total_income(self):
        return f"Доход с учётом премии: {sum(self._Worker__income.values())}"
    def __str__(self):
        return f"Полное имя сотрудника: {self.surname} {self.name}"

result = Position("Валерий", "Мухин", "инженер СТП", 70000, 12000)
print(result.get_full_name())
print(result.get_total_income())
print(result)

