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

import re


class Matrix:
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def get_readable_matrix_string(self, list_of_list):
        strings = []
        for row in list_of_list:
            strings.append(re.sub(r'\D', ' ', str(row)))

        return '\n'.join(strings)

    def __str__(self):
        return self.get_readable_matrix_string(self.list_of_list)

    def __add__(self, M):
        result = [[self.list_of_list[i][j] + M.list_of_list[i][j] for j in range(len(self.list_of_list[0]))] for i in range(len(self.list_of_list))]

        return Matrix(result)


m001 = Matrix([[1, 3, 6], [4, 8, 2], [11, 3, 1]])
m002 = Matrix([[4, 22, 7], [2, 3, 1], [14, 7, 3]])
m003 = Matrix([])
m003 = m001 + m002
print(m003)
