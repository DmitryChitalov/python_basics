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


class Worker:  # определяем базовый класс
    def __init__(self, name, surname, position, wage, bonus):
        # задаём публичные атрибуты
        self.name = name
        self.surname = surname
        self.position = position
        # задаём защищённый атрибут, ссылающийся на словарь
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):  # создаём новый класс на основе Worker
    def __str__(self):  # перегрузим метод __str__ для нашего класса
        return "Полное имя сотрудника: {0} {1} ".format(self.surname, self.name)

    def get_full_name(self):    # определяем метод для класса
        print(f'Полное имя сотрудника: {self.surname} {self.name}')

    def get_total_income(self): # определяем метод для класса
        print(f'Дохода с учетом премии: {self._income["wage"] + self._income["bonus"]}')


manager = Position('Иван', 'Петров', 'Менеджер', 50000, 20000)  # создаём объекта класса
senior_manager = Position('Михаил', 'Белов', 'Старший Менеджер', 70000, 25000)  # создаём объект класса
manager.get_full_name()     # используем свой метод
manager.get_total_income()
senior_manager.get_full_name()
senior_manager.get_total_income()
print(manager)  # вывод при помощи изменённого метода
print(senior_manager)