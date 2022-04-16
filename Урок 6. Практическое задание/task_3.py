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
    _income = {
        "wage": 0,
        "bonus": 0
    }

    name = None
    surname = None
    position = None

    def __init__(self, name, surname, position) -> None:
        self.name = name
        self.surname = surname
        self.position = position

    def set_income(self, wage, bonus) -> None:
        if type(wage) is int:
            self._income["wage"] = wage

        if type(bonus) is int:
            self._income["bonus"] = bonus

class Position(Worker):

    def __init__(self, name, surname, position) -> None:
        super().__init__(name, surname, position)

    def get_full_name(self) -> str:
        return f"{self.surname} {self.name}"

    def get_total_income(self) -> int:
        return self._income["wage"] + self._income["bonus"]
    
    def __str__(self) -> str:
        return str({
            "fullname": self.get_full_name(),
            "income": self.get_total_income()
        })


position_1 = Position("Ivan", "Ivanov", "Developer")
position_1.set_income(50000, 30000)
print(position_1)