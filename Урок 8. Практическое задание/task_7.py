"""
Задание 7.*

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""

class ComplexNumber:
    def __init__(self, c, d, *args):
        self.c = c
        self.d = d
        self.a = 'c + d * i'

    def __add__(self, other):
        print(f'Сумма a и b равна')
        return f'a = {self.c + other.c} + {self.d + other.d} * i'

    def __mul__(self, other):
        print(f'Произведение a и b равно')
        return f'a = {self.c * other.c - (self.d * other.d)} + {self.d * other.c} * i'

    def __str__(self):
        return f'a = {self.c} + {self.d} * i'


a_1 = ComplexNumber(3, -6)
a_2 = ComplexNumber(6, 8)
print(a_1)
print(a_1 + a_2)
print(a_1 * a_2)