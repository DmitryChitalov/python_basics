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
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'Полное имя сотрудника: {self.name} {self.surname}. Должность: {self.position}'

    def get_total_income(self):
        profit = self._income['wage'] + self._income['bonus']
        return f'Доход с учетом премии составил: {profit}'

    def __str__(self):
        return self.name, self.surname, self.position


a = Position('Стас', 'Стрельник', 'Инженер', 10000, 5000)
b = Position('Николай', 'Рудь', 'Мастер', 15000, 7000)
print(a.get_full_name())
print(a.get_total_income())
print(b.get_full_name())
print(b.name)
print(b.surname)
print(b.position)
print(b._income)
print(b.get_total_income())
print(b.__str__())
