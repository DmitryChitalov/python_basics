class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

class Position(Worker):

    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        print(f"Полное имя сотрудника - {self.name} {self.surname}")

    def get_total_income(self):
        total_income = 0
        for key, value in self._income.items():
            total_income += value
        print(f"Доход сотрудника равен {total_income}")

p = Position("Иван", "Сергеев", "водитель", {"оклад": 20000, "премия": 15000})
p.get_full_name()
p.get_total_income()
print(p.name)
print(p.surname)
print(p.position)