class Worker:
    def __init__(self,  name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        return "Полное имя сотрудника: " + self.name +" " + self.surname
    def get_total_income(self):
        return "Итоговый доход: " + str(float(self._income["wage"]) + float(self._income["bonus"]))

a = Position(input("Имя сотрудника: "), input("Фамилия: "), input("Должность: "), float(input("Оклад: ")), float(input("Премия: ")))
print("Атрибуты: ", a.name, a.surname, a.position, a._income)
print(a.get_full_name())
print(a.get_total_income())