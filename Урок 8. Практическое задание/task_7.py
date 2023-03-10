"""
Задание 7.*

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.compl = 'a + b * i'

    def __add__(self, other):
        print('Сумма n и m равна')
        return f'compl = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение n и m равно')
        return f'compl = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'compl = {self.a} + {self.b} * i'


n = ComplexNumber(14, -13)
m = ComplexNumber(32, 41)
print(n)
print(n + m)
print(n * m)
