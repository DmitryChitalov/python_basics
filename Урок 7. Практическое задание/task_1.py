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
    def __init__(self, my_matrix):
        self.my_matrix = my_matrix

    def __str__(self):
        for i in range(0, len(self.my_matrix)):
            for j in range(0, len(self.my_matrix[i])):
                print(self.my_matrix[i][j], end=' ')
            print()
        return ' '

    def __add__(self, other):
        matrix_temp = self.my_matrix
        for i in range(0, len(matrix_temp)):
            for j in range(0, len(matrix_temp[i])):
                matrix_temp[i][j] = self.my_matrix[i][j] + other.my_matrix[i][j]
        return Matrix(matrix_temp)



a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

a_matrix = Matrix(a)
b_matrix = Matrix(b)
print("---------Matrix 1----------")
print(a_matrix)
print("---------Matrix 2----------")
print(b_matrix)
print("---------Matrix 1 + 2 ----------")
print(a_matrix + b_matrix)
