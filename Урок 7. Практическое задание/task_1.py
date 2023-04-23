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

import random


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        for row in self.matrix:
            for i in row:
                print(f'{i:4}', end='')
            print()

    def __add__(self, other):
        for i in range(len(self.matrix)):
            for j in range(len(other.matrix[i])):
                self.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix.__str__(self)


my_matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
next_matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
my_matrix.__str__()
print()
next_matrix.__str__()
print()
new_matrix = my_matrix + next_matrix
