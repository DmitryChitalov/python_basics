"""
Задание 7.*

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""

class ComplexNum():
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        first_num = self.num.split()
        second_num = other.num.split()
        return f'{(int(first_num[0]) + int(second_num[0]))} + {int(first_num[2][:-1]) + int(second_num[2][:-1])}i '

    def __mul__(self, other):
        first_num = self.num.split()
        second_num = other.num.split()
        a = int(first_num[0])
        b = int(first_num[2][:-1])
        c = int(second_num[0])
        d = int(second_num[2][:-1])
        return f'{a * c - b * d} + {b * c + a * d}i'


first = ComplexNum('13 + 2i')
second = ComplexNum('24 + 8i')

print(first + second)
print(first * second)
