class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}
class Position(Worker):
    def get_full_name(self):
        return (f'{self.name}, {self.surname}')

    def get_total_income(self):
       return self._income['wage'] + self._income['bonus']

    def __str__(self):
        return (f'Сотрудник: {self.get_full_name()}, доход: {self.get_total_income()}')

my_worker1 = Position ('Иван', 'Иванов', 'продавец', 20000, 5000)
my_worker2 = Position ('Петр', 'Петров', 'кассир', 20000, 2000)
print(my_worker1.get_full_name(), my_worker1.get_total_income())
print(my_worker2.get_full_name(), my_worker2.get_total_income())
print(my_worker1)
print(my_worker2)