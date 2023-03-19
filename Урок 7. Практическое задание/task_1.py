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


class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join([''.join(['%d\t' % i for i in row]) for row in self.matrix])

    def __add__(self, other):
        if len(self.matrix) == len(other.matrix):
            lenght = len(self.matrix[0])
            for row in self.matrix:
                if len(row) != lenght:
                    raise MatrixError(self, other)
            for row2 in other.matrix:
                if len(row2) != lenght:
                    raise MatrixError(self, other)
            result = []
            mat_row = []
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    total = other.matrix[i][j] + self.matrix[i][j]
                    mat_row.append(total)
                    if len(mat_row) == len(self.matrix[0]):
                        result.append(mat_row)
                        mat_row = []
            return Matrix(result)
        else:
            raise MatrixError(self, other)


mat = [[1, 1, 1, 1], [1, 1, 75, 1], [1, 1, 1, 1]]
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
matr_a = Matrix(matrix)
matr_b = Matrix(mat)

res = matr_a + matr_b
print(res)
