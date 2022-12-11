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
    """Базовый класс"""
    name: str
    surname: str
    position: str
    _income: dict

    def total_income(self):
        """Базовый расчет дохода с учетом сорока часовой недели"""

        total = self._income.get('wage') * 40

        if self._income.get('bonus'):
            total += self._income.get('bonus')

        return total

    def __str__(self):
        return f'Способ вывода через "__str__" - {self.name} {self.surname}'


class Position(Worker):
    """Класс Position"""

    def income(self, salery: dict):
        """Зарплата сотрудника"""
        self._income = salery

    def get_full_name(self):
        """Полное имя сотрудника"""
        return f'Сотрудника зовут - {self.name} {self.surname}'

    def get_total_income(self):
        """Дохос, с учетом премии"""
        return f"Доход в неделю составил - {self.total_income()} р."


person = Position()
person.name = "Майк"
person.surname = "Сваровский"
person.position = "Программист"
person.income({'wage': 377, 'bonus': 1110})

print(person.get_full_name())
print(person.__str__())
print(person.get_total_income())
