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

П.С. попытайтесь добиться вывода информации о сотруднике также через перегрузку __str__
__str__(self) - вызывается функциями str, print и format. Возвращает строковое представление объекта.
"""
d = {"wage": 10000, "bonus": 5000}


class Worker:
    name = "Владимир"
    surname = "Валерьянов"
    position = "Менеджер"
    _income = d


class Position(Worker):

    def get_full_name(self):
        print(f'ФИО: {self.surname} {self.name} - {self.position}')

    def get_total_income(self):
        print(f'Зарплата сотрудника: {self._income["wage"] + self._income["bonus"]}')

    def __str__(self):
        return f'ФИО: {self.surname} {self.name} - {self.position} \n' \
               f'Зарплата сотрудника: {self._income["wage"] + self._income["bonus"]}'


task_3 = Position()
task_3.get_full_name()
task_3.get_total_income()
print(task_3)
