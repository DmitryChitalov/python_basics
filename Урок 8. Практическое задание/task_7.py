"""
Задание 7.*

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class ComplexNumbers:
    def __init__(self, real, imag):
        self.__complex = complex(real, imag)

    def __add__(self, other):
        var1 = other.__complex
        var1 = self.__complex + var1
        return ComplexNumbers(var1.real, var1.imag)

    def __mul__(self, other):
        var1 = other.__complex
        var1 = self.__complex * var1
        return ComplexNumbers(var1.real, var1.imag)

    def __str__(self):
        return self.__complex.__str__()


c = ComplexNumbers(1, 2)
c1 = ComplexNumbers(2,1)
print(c + c1)
print(c * c1)
print()