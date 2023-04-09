class Worker:
    name: str
    surname: str
    position: str
    _income: dict

    def __init__(self, name: str, surname: str, position: str, wage: int, bonus: int):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {
            "wage": wage,
            "bonus": bonus
        }


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return sum(self._income.values())


john = Position("John", "Doe", "Developer", 2000, 800)
print(john.get_full_name(), john.get_total_income())

artur = Position("Artur", "Doe", "Developer", 1800, 800)
print(artur.get_full_name(), artur.get_total_income())