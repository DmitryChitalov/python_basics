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
        return f'SN: {self.surname} {self.name}'

    def get_total_income(self):
        return sum(self._income.values())


if __name__ == '__main__':
    me = Position('Slava', 'Merlow', 'Support engineer', 70000, 14500)
    me1 = Position('Stas', 'Karnavich', 'Python developer', 83000, 21000)
    print(me.position)
    print(me.get_full_name())
    print(f'Total income: {me.get_total_income()}')
    print(me._income)
    print("///////////")
    print(me1.position)
    print(me1.get_full_name())
    print(f'Total income: {me1.get_total_income()}')
    print(me1._income)

