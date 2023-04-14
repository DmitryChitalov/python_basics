"""
Задание 1.

Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init()__),
который должен принимать данные (список списков) для формирования матрицы.
[[], [], []]
Следующий шаг — реализовать перегрузку метода __str()__ для вывода матрицы в привычном виде.

Далее реализовать перегрузку метода __add()__ для реализации операции
сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.

Пример:
1 2 3
4 5 6
7 8 9

1 2 3
4 5 6
7 8 9

Сумма матриц:
2 4 6
8 10 12
14 16 18
"""

# import numpy as np

class Matrix:

    def __init__(self, param):
        self.array = param

    def __str__(self, *args):
        return f"{self.array}"

    def __add__(self, other):
        res = [[self.array[j][i] + other.array[j][i] for i in range(len(self.array[0]))] for j in range(len(self.array))]
        return Matrix(res)


m1 = Matrix([[3, 5, 32, 13], [2, 4, 6, 8], [51, 86, -5, 11]])
m2 = Matrix([[31, 32, 51, 86], [26, 14, -16, 18], [-1, 64, -8, 33]])
print(f"Первая матрица: {m1}")
print(f"Вторая матрица: {m2}")
print(f"Сумма матриц: {m1 + m2}")

