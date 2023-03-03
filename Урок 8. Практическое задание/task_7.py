"""
Задание 7.*

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""

class ComplexNum:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'Сумма равна = {self.a + other.a} + {self.b + other.b}i'


    def __mul__(self, other):
        return f'Результат умножения: {(self.a * other.a) - (self.b * other.b)} ' \
               f'{self.b * other.a}i'

    def __str__(self):
        return f'{self.a}{"+" if self.b > 0 else ""}{self.b}i'

f_numbs = ComplexNum(5, -7)
sec_numbs = ComplexNum(15, 10)
print(f_numbs + sec_numbs)
print(f_numbs * sec_numbs)
