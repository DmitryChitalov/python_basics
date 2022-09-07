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
    name = "Иван"
    surname = "Кочевников"
    position = "Строитель своего тела"
    _income = {"wage": 150000, "bonus": 13000}

    def __str__(self):
        print("WORKER str")
        return str(f"Сотрудник: {self.name} {self.surname}, с окладом: {self._income['wage'] + self._income['bonus']}")

    def __format__(self, format_spec):
        print("WORKER format")
        return format(f"Сотрудник: {self.name} {self.surname}, с окладом: {self._income['wage'] + self._income['bonus']}")


class Position(Worker):
    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

    def set_income_wage(self, wage):
        self._income["wage"] = wage

    def set_income_bonus(self, bonus):
        self._income["bonus"] = bonus

    def __init__(self, name, surname, my_position):
        self.name = name
        self.surname = surname
        self.position = my_position

    def __str__(self):
        print("Position str")
        return str(f"Сотрудник: {self.get_full_name()}, с окладом: {self.get_total_income()}")

    def __format__(self, format_spec):
        print("Position format")
        return format(f"Сотрудник: {self.get_full_name()}, с окладом: {self.get_total_income()}")


worker = Worker()
print(worker)
print(str(worker))
print(format(worker))

position = Position("Игорь", "Боровиков", "Инженер-технолог")
position.set_income_wage(12345)

print(position)
print(str(position))
print(format(position))
