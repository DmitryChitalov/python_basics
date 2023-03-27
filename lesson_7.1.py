"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
"""


class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        new_matrix = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]

        for i in range(len(self.list_1)):
            for j in range(len(self.list_2[i])):
                new_matrix[i][j] = self.list_1[i][j] + self.list_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in new_matrix]))

    def __str__(self):
        new_matrix = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in new_matrix]))


my_matrix = Matrix([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]],
                   [[9, 8, 7],
                    [6, 5, 4],
                    [3, 2, 1]])

print(my_matrix.__add__())
