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
    def __init__(self, in_matrix):
        self.in_matrix = in_matrix

    def __str__(self):
        return '\n'.join(' '.join([str(i) for i in el]) for el in self.in_matrix)

    def __add__(self, other):
        if len(self.in_matrix) != len(other.in_matrix):
            return 'Сложение невозможно, матрицы не равны'
        for el_1, el_2 in zip(self.in_matrix, other.in_matrix):
            if len(el_1) != len(el_2):
                return 'Сложение невозможно, матрицы не равны'
        m3 = [[x + y for x, y in zip(el_1, el_2)] for el_1, el_2 in zip(self.in_matrix, other.in_matrix)]
        return Matrix(m3)


matrix_1 = Matrix([[1, 2, 3], [4, 5, 6]])
matrix_2 = Matrix([[-1, -2, -3], [-4, -5, -6]])
print(matrix_1, end='\n\n')
print(matrix_2, end='\n\n')
print(matrix_1 + matrix_2)
