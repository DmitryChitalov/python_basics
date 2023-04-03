"""
Задание 7.*

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""

class CompNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        print(f'Сложение экземпляров: ')
        return f'x = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Умножение экземпляров: ')
        return f'x = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        print(f'Созданный экземпляр: ')
        return f'x = {self.a} + {self.b} * i'


x_1 = CompNumber(3, -8)
x_2 = CompNumber(7, 7)
print(x_1)
print(x_2)
print(x_1 + x_2)
print(x_1 * x_2)