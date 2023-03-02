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
    
    def __init__(self, name, surname, position, wage = 0, bonus = 0):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}
    
    

class Position(Worker):
    
    def get_full_name(self):
        return f'{self.surname} {self.name}'
    
    def get_total_income(self):
        return sum(self._income.values())
    
    def __str__(self):
            name = f'Имя: {position_worker_1.name}'
            surname = f'Фамилия: {position_worker_1.surname}'
            position = f'Должность: {position_worker_1.position}'
            full_name = f'Фамилия и имя: {position_worker_1.get_full_name()}'
            total_income = f'Доход: {position_worker_1.get_total_income()}'
            return f'{name}\n{surname}\n{position}\n{full_name}\n{total_income}'
            
    
position_worker_1 = Position('Иван', 'Иванов', 'рабочий', 100, 20)

print(position_worker_1.__str__())
 
        