# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных:
# создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.

class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': 100000, 'bonus': 2000}


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_full_salary(self):
        return self._income['wage'] + self._income['bonus']


v_pet = Position('Иван', 'Иванов', 'аналитик')
print(f'Новые данные: {v_pet.name}, {v_pet.surname}, {v_pet.position}, {v_pet._income}')
print(f'Полная зарплата {v_pet.get_full_name()} = {v_pet.get_full_salary()} рублей')

