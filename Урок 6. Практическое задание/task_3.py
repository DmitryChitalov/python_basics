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

П.С. попытайтесь добиться вывода информации о сотруднике также через перегрузку __str__
__str__(self) - вызывается функциями str, print и format. Возвращает строковое представление объекта.
"""


class Worker:
    def __init__(self, in_name, in_surname, in_pos, in_wage, in_bonus):
        self.name = in_name
        self.surname = in_surname
        self.position = in_pos
        self._income = {"wage": in_wage, "bonus": in_bonus}


class Position(Worker):
    def __init__(self, in_name, in_surname, in_pos, in_wage, in_bonus):
        super().__init__(in_name, in_surname, in_pos, in_wage, in_bonus)

    def __str__(self):  # перегрузка страндартного метода для изменения строкового представления объекта класса
        self.str1 = f"Полное имя работника: {self.name} {self.surname}"
        self.str2 = f"его полный доход: {self._income.get('wage') + self._income.get('bonus')}"
        return f"{self.str1}; {self.str2}"

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._income.get("wage") + self._income.get("bonus")


inp_name = input("Введите имя работника: ")
inp_surname = input("Введите фамилию работника: ")
inp_pos = input("Введите должность работника: ")
inp_wage = int(input("Введите оклад работника: "))
inp_bonus = int(input("Введите бонус работника: "))
pos_obj = Position(inp_name, inp_surname, inp_pos, inp_wage, inp_bonus)
print(f"Имя: {pos_obj.name}")
print(f"Фамилия: {pos_obj.surname}")
print(f"Должность: {pos_obj.position}")
print(f"Полное имя работника: {pos_obj.get_full_name()}")
print(f"Доход работника: {pos_obj.get_total_income()}")

# вывод с помощью перегрузки метода __str__
print(pos_obj)
