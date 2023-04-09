class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.surname} {self.name}"

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


john = Position("Игорь", "Иванов", "Менеджер", 50000, 10000)
print(john.name)  # Игорь
print(john.get_full_name())  # Иванов Игорь
print(john.position)  # Менеджер
print(john.get_total_income())  # 60000