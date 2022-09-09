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
    inner_matrix = None

    def __init__(self, matrix):
        self.inner_matrix = matrix

    def __str__(self):
        matrix_as_string = ""
        for el in self.inner_matrix:
            for inner_el in el:
                matrix_as_string += str(inner_el) + " "
            matrix_as_string += "\n"
        return matrix_as_string

    def __add__(self, other):
        merged_matrix = []
        for i in range(len(self.inner_matrix)):
            list_simple = []
            for j in range(len(self.inner_matrix[i])):
                list_simple.append(self.inner_matrix[i][j] + other.inner_matrix[i][j])
            merged_matrix.append(list_simple)
        return merged_matrix


list_of_the_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

matrix_a = Matrix(list_of_the_list)
matrix_b = Matrix(list_of_the_list)

matrix_c = Matrix(matrix_a + matrix_b)
print(matrix_c)
