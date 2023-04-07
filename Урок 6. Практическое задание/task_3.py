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
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'Полное имя сотрудника: {self.surname} {self.name}'

    def get_total_income(self):
        return f'Доход с учетом премии: {sum(self._income.values())}'

    def __str__(self):
        return f'Полное имя сотрудника: {self.surname} {self.name}'


if __name__ == '__main__':
    worker_1 = Position('Николай', 'Иванов', 'Инженер 2 разряда', 93000, 12000)
    worker_2 = Position('Сергей', 'Петров', 'Инженер 3 разряда', 72000, 7000)
    worker_3 = Position('Геннадий', 'Сидоров', 'Инженер', 51000, 5000)
    print(worker_1.get_full_name())
    print(worker_1.get_total_income())
    print(worker_2.get_full_name())
    print(worker_2.get_total_income())
    print(Position('Геннадий', 'Петров', 'Инженер', 51000, 5000))
    print(worker_3.get_total_income())
