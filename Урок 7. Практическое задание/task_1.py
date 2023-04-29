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
    '''создание атрибута matrix для класса'''
    def __init__(self, matrix):
        self.matrix = matrix
    def __str__(self):
        m = ''
        for a in range(len(self.matrix)):
            m = m + ' '.join(map(str, self.matrix[a])) + '\n'
        return m
    def __add__(self, other):
        if len(self.matrix) != len(other.matrix):
            return None
        summ = self.matrix
        for a in range(len(self.matrix)):
            for b in range(len(self.matrix[a])):
                summ[a][b] = self.matrix[a][b] + other.matrix[a][b]
        return Matrix(summ)

mat1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mat2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
summ1 = Matrix(mat1)
summ2 = Matrix(mat2)
print(f'Значения матрицы 1: ')
print(summ1)
print(f'Значения матрицы 2: ')
print(summ2)
result = summ1 + summ2
print(f'Сумма двух матриц равна: ')
print(result)