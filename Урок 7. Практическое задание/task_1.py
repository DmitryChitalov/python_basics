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
some_matrix = [[31, 22], [37, 43], [51, 86]]
matrix_to_add_1 = [[5, 18, 11], [6, 17, 23], [41, 50, 9]]
matrix_to_add_2 = [[45, 8, 2],  [6, 7, 93], [24, 5, 97]]


class Matrix:
    container: list

    def __init__(self, matrix: list):
        self.container = matrix

    def __str__(self):
        result = 'Matrix:\n'
        for row in self.container:
            row_str = '\t'.join(map(str, row))
            result += row_str + '\n'
        return result

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError('Cannot add matrix and non-matrix types')
        if not self.container or len(self.container) != len(other.container) or \
                len(other.container[0]) != len(self.container[0]):
            raise IndexError('Matrices have different dimensions')
        new_matrix = []
        for i in range(len(self.container)):
            new_matrix.append([])
            for j in range(len(self.container[i])):
                new_matrix[i].append(self.container[i][j] + other.container[i][j])
        return Matrix(new_matrix)


matrix1 = Matrix(some_matrix)
print(matrix1)

first_matrix = Matrix(matrix_to_add_1)
print(first_matrix)
second_matrix = Matrix(matrix_to_add_2)
print(second_matrix)

try:
    print(matrix1 + first_matrix)
except BaseException as err:
    print(f"Unexpected {err=}, {type(err)=}\n")

result_matrix = first_matrix + second_matrix
print(f'Result {result_matrix}')
