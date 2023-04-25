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
from copy import deepcopy


class Matrix:
    def __init__(self, mass):
        self.mass = mass

    def __str__(self):
        result_table = ''
        for i in range(len(self.mass)):
            result_table += f'{" ".join(str(x) for x in self.mass[i])}\n'
        return result_table

    def __add__(self, other):
        res_list = deepcopy(other.mass)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        for inx, val in enumerate(self.mass):
            for j_inx, j_val in enumerate(val):
                res_list[inx][j_inx] += self.mass[inx][j_inx]
        return Matrix(res_list)


mx1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
mx2 = Matrix([[3, 2, 1], [6, 5, 4], [9, 8, 7]])
mx3 = mx1 + mx2
print(f'Матрица 1:\n{mx1}')
print(f'Матрица 2:\n{mx2}')
print(f'Сумма матриц:\n{mx3}')
