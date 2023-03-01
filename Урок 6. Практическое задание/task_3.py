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
    Хранит данные о работнике

    Attributes:
        name       имя работника
        surname    фамилия работника
        position   должность работника
        _income    словарь, содержащий элементы: оклад и премия
    """
    name = ''
    surname = ''
    position = ''
    _income = {'wage': 0, 'bonus': 0}

    def __str__(self):
        return f"{self.name}, {self.surname}, {self._income}"


class Position(Worker):
    """
    Реализует получение данных о работнике
    """

    def get_full_name(self, **kwargs):
        """
        Присваивает сотруднику полноe имя

        :param kwargs:
                str name: имя сотрудника,
                str surname фамилия сотрудника
        :return: None
        """

        self.name = kwargs.get('name')
        self.surname = kwargs.get('surname')

    def get_total_income(self, **kwargs):
        """
        Присваивает сотруднику доход с учетом премии

        :param kwargs:
                float wage: доход,
                float bonus: премия
        :return: None
        """

        self._income = {'wage': kwargs.get('wage'), 'bonus': kwargs.get('bonus')}


position_0 = Position()
position_1 = Position()

position_0.get_full_name(name='Иван', surname='Иванов')
position_0.get_total_income(wage=35256.23, bonus=13244)
position_1.get_full_name(name='Борис', surname='Волков')
position_1.get_total_income(wage=45256.23, bonus=14578)

print(f"{position_1.name} {position_1.surname} {position_1._income}")
print(f"{position_0.name} {position_0.surname} {position_0._income}\n")

print(position_0)
print(position_1)
