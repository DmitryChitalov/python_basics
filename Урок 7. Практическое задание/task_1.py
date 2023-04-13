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
from functools import reduce


class Matrix:

    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        new_list = ""
        for el in self.my_list:
            new_list += " ".join(map(str, el)) + "\n"
        return new_list

    def __add__(self, result):
        matrix_sum = []
        for el1, el2 in zip(self.my_list, result.my_list):
            ind_sum = []
            for ind1, ind2 in zip(el1, el2):
                ind_sum.append(int(ind1) + int(ind2))
            matrix_sum.append(ind_sum)
        return Matrix(matrix_sum)


matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(f"Первая матрица: \n{matrix_1}")
print(f"Вторая матрица: \n{matrix_2}")
print(f"Сумма матриц: \n{matrix_1 + matrix_2}")

