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
    def __init__(self, *param):
        self.matrix = []
        self.matrix.append(param)

    def __str__(self):
        result = ''
        for el in self.matrix[0]:
            result += f"{el} \n"
        return result

    def __add__(self, other):
        result = []
        for i in range(0, len(self.matrix[0])):
            el_new = []
            for j in range(0, len(self.matrix[0][i])):
                el_new.append(self.matrix[0][i][j] + other.matrix[0][i][j])
            result.append(el_new)
        return result


matrix1 = Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
matrix2 = Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
matrix_sum = matrix1 + matrix2

for el in matrix_sum:
    print(f"{el}")
