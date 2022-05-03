class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return int(self._income['wage']) + int(self._income['bonus'])


a = Position("igor", "mkrtchan", "lord", "1000", "500000")
print(f"Сотрудник {a.get_full_name()} имеет доход {a.get_total_income()} тенге")
