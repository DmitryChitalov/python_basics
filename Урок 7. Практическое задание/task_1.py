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
    def __init__(self, i, matrix):
        self.matrix_num = i
        self.matrix = matrix

    def __str__(self):
        mrx = ''
        for a in range(len(self.matrix)):
            mrx = mrx + '\t'.join(map(str, self.matrix[a])) + '\n'
        return f"Матрица {self.matrix_num}:\n{mrx}"

    def __add__(self, other):
        res = self.matrix
        res_m = ''
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                res[i][j] = self.matrix[i][j] + other.matrix[i][j]
        for a in range(len(res)):
            res_m = res_m + '\t'.join(map(str, res[a])) + '\n'
        return f"Сумма матриц:\n{res_m}"


mat_1 = Matrix(1, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(mat_1)
mat_2 = Matrix(2, [[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print(mat_2)
res = mat_1 + mat_2
print(res)
