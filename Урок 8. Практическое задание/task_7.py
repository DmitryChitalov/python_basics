"""
Задание 7.*

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class ComplexNumber:
    def __init__(self, x, y):
        self.c = complex(x, y)
        self.new_c = 0

    def __add__(self, other):
        self.new_c = self.c + other.c
        return self.new_c

    def __mul__(self, other):
        self.new_c = self.c * other.c
        return self.new_c


c_1 = ComplexNumber(1, 1)
c_2 = ComplexNumber(1, 1)

print(c_1 + c_2)
print(c_1 * c_2)
