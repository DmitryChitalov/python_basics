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
import copy


class Matrix:
    def __init__(self, matrix_data):
        self.matrix_data = matrix_data

    def __str__(self):
        s = ''
        for i in range(len(self.matrix_data)):
            s = s + '\t'.join(map(str, self.matrix_data[i])) + '\n'
        return s

    def __add__(self, other):
        if len(self.matrix_data) != len(other.matrix_data):
            return None
        res = copy.deepcopy(self.matrix_data)
        for i in range(len(self.matrix_data)):
            for k in range(len(self.matrix_data[i])):
                res[i][k] = self.matrix_data[i][k] + other.matrix_data[i][k]
        return Matrix(res)


matrix_list1 = [[1,2,3],[4,5,6]]
matrix_list2 = [[7,8,9],[10,11,12]]
m1 = Matrix(matrix_list1)
m2 = Matrix(matrix_list2)
print(m1)
print(m2)
print(m1 + m2)



