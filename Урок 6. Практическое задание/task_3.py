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
    Worker storage
    """
    name = str()
    surname = str()
    position = str()
    _income = {'wage': None, 'bonus': None}

    def __init__(self, name, surname, position, wage, bonus):
        """
        :param name: str
        :param surname: str
        :param position: str
        :param wage: wage
        :param bonus: bonus
        """
        self.position = position
        self.name = name
        self.surname = surname
        self._income['wage'] = wage
        self._income['bonus'] = bonus


class Position(Worker):
    """
    Position storage
    """

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return sum(self._income.values())


if __name__ == '__main__':
    pos = Position('Ivan', 'Ivanov', 'student', 110000, 15000)

    print(pos.get_full_name())
    print(pos.get_total_income())
