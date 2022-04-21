"""
Задание 7.*

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class MyComplex:
    def __init__(self, real, imag=0):
        self.__complex = complex(real, imag)

    def __add__(self, other):
        if isinstance(other, MyComplex):
            other = other.__complex

        complex_ = self.__complex + other
        return MyComplex(complex_.real, int(complex_.imag))

    def __mul__(self, other):
        if isinstance(other, MyComplex):
            other = other.__complex

        complex_ = self.__complex * other
        return MyComplex(complex_.real, int(complex_.imag))

    def __str__(self):
        return self.__complex.__str__()


if __name__ == '__main__':
    c1 = MyComplex(2, -3)
    c2 = MyComplex(5)

    print(c1 + c2, complex(2, -3) + complex(5))
    print(c1 * c2, complex(2, -3) * complex(5))