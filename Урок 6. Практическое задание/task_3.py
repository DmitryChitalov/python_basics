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

# Выводим задание для программы
print(f'\nРеализовать базовый класс Worker (работник),\n'
      f'в котором определить публичные атрибуты name, surname, position (должность),\n\n'
      f'и защищенный атрибут income (доход). Последний атрибут должен ссылаться\n'
      f'на словарь, содержащий элементы: оклад и премия, например, ''{''"wage": wage, "bonus": bonus''}''.\n')

"""Создаем класс Worker"""
class Worker:
    def __init__(self, name: str, surname: str, position: str, wage: float, bonus: float):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'Оклад': wage, 'Премия': bonus}


"""Создаем класс Position"""
class Position(Worker):
    def __init__(self, name: str, surname: str, position: str, wage: float, bonus: float):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):  # Метод возврат полного имени и фамилии
        return f'{self.name} {self.surname}'

    def get_total_income(self):  # Метод возврат суммы зарплаты и премии
        return self._income['Оклад'] + self._income['Премия']

    def __str__(self):  # Метод __str__
        return f'Заработная плата {self.name} {self.surname} составляет {"{:.2f}".format(self.get_total_income())} руб.'

""" Объявляем переменные и выводим данные с помощью методов класса"""
worker_info = Position('Иван', 'Иванов', 'Специалист', 11000, 11000)
print(f'Заработная плата {worker_info.name} {worker_info.surname} составляет '
      f'{"{:.2f}".format(worker_info.get_total_income())} руб.')
print(worker_info)
