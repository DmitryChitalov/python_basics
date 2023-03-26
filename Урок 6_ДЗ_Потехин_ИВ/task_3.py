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
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')

    def __str__(self):
        return f'ФИО сотрудника: {self.name} {self.surname}; должность: {self.position}' \
               f'; доход: {str(self._income.get("wage") + self._income.get("bonus"))}.'


# клиентский код
person = Position('Иван', 'Сидоров', 'рабочий', 30000, 20000)
person2 = Position('Федор', 'Тихонов', 'строитель', 50000, 30000)
print(person.get_full_name())
print(person.position)
print(person.get_total_income())
print(f'\n{person.__str__()}')

print(person2.get_full_name())
print(person2.position)
print(person2.get_total_income())
print(f'\n{person2.__str__()}')
