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
(self) - вызывается функциями str, print и format. Возвращает строковое представление объекта.
"""


class Worker:
    def __init__(
            self,
            name: str,
            surname: str,
            position: str,
            wage: float = 0,
            bonus: float = 0
    ):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return self.__str__()

    def get_total_income(self):
        return sum(self._income.values())

    def __str__(self):
        return f'{self.name} {self.surname} - {self.position}'


if __name__ == '__main__':
    position_1 = Position('Ivan', 'Ivanov', 'developer', 10000, 500)
    print(position_1.get_full_name())
    print(position_1.get_total_income())

    print()

    position_2 = Position('Stepan', 'Stepanov', 'dishwasher', 5000, 1500)
    print(position_2.get_full_name())
    print(position_2.get_total_income())
