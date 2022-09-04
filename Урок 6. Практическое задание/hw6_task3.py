class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']

    def __str__(self):
        return f"ИФ: {self.get_full_name()} \nДолжность: {self.position} \nОклад: {self.get_total_income()} \n"


w = Position('Иван', 'Иванов', 'специалист', 60000, 20000)
print(w)

w2 = Position('Петр', 'Петров', 'рекрутер', 50000, 15000)
print(w2)
