"""
Задание 7.*

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class ComplexDigit:
    def __init__(self, n_p, c_p):
        self.n_p = n_p
        self.c_p = c_p
        self.complex_digit = complex(n_p, c_p)

    def __add__(self, other):
        res = self.complex_digit + other.complex_digit
        return complex(res)

    def __mul__(self, other):
        res = self.complex_digit * other.complex_digit
        return complex(res)


var_1 = ComplexDigit(5, -1)
var_2 = ComplexDigit(10, 2)
var_3 = ComplexDigit(12, 2)
print(var_1 + var_2)
print(var_1 + var_3)
print(var_1 * var_2)
print(var_1 * var_3)
"""
Проверка:
(15+1j)
(17+1j)
(52+0j)
(62-2j)
"""
