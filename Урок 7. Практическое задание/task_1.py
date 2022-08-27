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
    def __init__(self, *matrix):
        self.matrix_list = list(matrix)

    def __str__(self):
        result = '\n'.join(map(str, self.matrix_list)).replace(',', '').replace('[', '').replace(']', '')
        return result

    def __add__(matrix1, matrix2):
        matrix_sum = []
        line_sum = []
        for x in range(len(matrix1.matrix_list)):
            for y in range(len(matrix1.matrix_list[x])):
                line_sum.append(matrix1.matrix_list[x][y] + matrix2.matrix_list[x][y])
            matrix_sum.append(line_sum)
            line_sum = []
        return Matrix('\n'.join(map(str, matrix_sum)))


matrixes = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix1_obj = Matrix(matrixes[0], matrixes[1])
matrix2_obj = matrix1_obj
print(f" {matrix1_obj} \n+\n {matrix2_obj} \n=\n {matrix1_obj + matrix2_obj}")
