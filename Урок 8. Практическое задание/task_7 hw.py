__author__ = 'AndreiM'
__version__ = "1.0 25.04.2023"
print("\n task_7 \n -------- \n")


import math

class ComplexNum:
    def __init__(self, x, y, *args):
        self.x = x
        self.y = y
        self.z = 'x + y * j'

    def __add__(self, n):
        print(f'Сумма z_1 и z_2 равна')
        return f'z = {self.x + n.x} + {self.y + n.y}j'

    def __mul__(self, n):
        print(f'Произведение z_1 и z_2 равно')
        return f'z = {self.x * n.x - self.y * n.y} + {self.x * n.y + n.x * self.y}j'

    def __str__(self):
        return f'z = {self.x} + {self.y}j'


z_1 = ComplexNum(4, -2)
z_2 = ComplexNum(-2, 6)
print('Комплексное число z_1  ', z_1)
print('Комплексное число z_2  ', z_2)
print(z_1 + z_2)
print(z_1 * z_2)
print('complex(1, 1) + complex(1, 1) with math =  ', complex(4, -2) + complex(-2, 6))
print('complex(2, 4) * complex(2, 5) with math =  ', complex(4, -2) * complex(-2, 6))
print('complex(1.2e-2, 2.0) * complex(-2, 6) with math =  ', complex(1.2e-2, 2.0) * complex(-2, 6))
print('complex(1.2e-2, 2.0) + complex(-2, 6) with math =  ', complex(1.2e-2, 2.0) + complex(-2, 6))

"""
Задание 7.*

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""