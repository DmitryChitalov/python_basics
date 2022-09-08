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

class Worker():
    def __init__(self, name: str, surname: str, position: str, wage: float, bonus: float):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        return ' '.join(sorted([self.name, self.surname]))

    def get_total_income(self):
        return sum(self._income.values())

if __name__ == '__main__':
    position_data =[
        {
            'name': 'Владимир',
            'surname': 'Смирнов',
            'position': 'Инженер-электрик',
            'wage':  40000,
            'bonus': 0
        },
        {
            'name': 'Александр',
            'surname': 'Кузнецов',
            'position': 'Специалист по инф.безопасности',
            'wage': 100000,
            'bonus': 20000
        },
        {
            'name': 'Мария',
            'surname': 'Волкова',
            'position': 'HR-Менеджер',
            'wage': 60000,
            'bonus': 15000
        }
    ]
    for item in position_data:
        position = Position(**item)
        print('Имя: ', position.name)
        print('Фамилия: ', position.surname)
        print('Полное имя: ', position.get_full_name())
        print('Должность: ', position.position)
        print('Суммарный доход: ', position.get_total_income())
        print('\n')

