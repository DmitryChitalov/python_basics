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
        x = ''
        for i in range(len(self.matrix)):
            x = x + '\t'.join(map(str, self.matrix[i])) + '\n'
        return x

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix):
            return None
        sum = self.matrix
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                sum[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix(sum)


matrix_1 = [[2, 3, 1, 7], [4, 6, 8, 4], [10, 8, 5, 2]]
matrix_2 = [[12, 3, 7, 2], [1, 5, 6, 6], [11, 9, 3, 0]]
matrx_1 = Matrix(matrix_1)
matrx_2 = Matrix(matrix_2)
print(f'Матрица 1: ')
print(matrx_1)
print(f'Матрица 2: ')
print(matrx_2)
res = matrx_1 + matrx_2
print(f'Сумма двух матриц: ')
print(res)