"""
Задание 7.*

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""

class ComplexNumbers:
    def __init__(self, a, b):
        self.c = complex(a, b)
        self.new_c = 0

    def __add__(self, other):
        self.new_c = self.c + other.c
        return self.new_c

    def __mul__(self, other):
        self.new_c = self.c * other.c
        return self.new_c


c_1 = ComplexNumbers(1, 2)
c_2 = ComplexNumbers(1, 2)

print(c_1 + c_2)
print(c_1 * c_2)
