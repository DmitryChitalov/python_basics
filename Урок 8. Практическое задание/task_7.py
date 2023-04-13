"""
Задание 7.*

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class ComplexNumber:

    def __init__(self, complex_num):
        self.complex_num = complex(complex_num)

    def __add__(self, other):
        return ComplexNumber(self.complex_num + other.complex_num)

    def __mul__(self, other):
        return ComplexNumber(self.complex_num * other.complex_num)


num1 = ComplexNumber('3+5j')
num2 = ComplexNumber('2+2j')

summ = num1 + num2
print(summ.complex_num)
composition = num1 * num2
print(composition.complex_num)
