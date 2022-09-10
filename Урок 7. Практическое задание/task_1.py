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

# Импортируем модуль подбора случайных чисел
from random import randrange

# Выводим на экран задание
print('\nУрок 7 Задание 1\n')

# Определяем класс и методы
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix(self.matrix)

    def __str__(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                print(f'{"{:3}".format(self.matrix[i][j])} ', end='')
            print()
        return ''

# Определяем функцию формирования матрицы из случайных чисел
def random_matrix(line, collunm):
    matrix = []
    matrix_line = []
    for i in range(0, line):
        for j in range(0, collunm):
            rand = randrange(10)
            matrix_line.append(rand)
        matrix.append(matrix_line)
        matrix_line = []
    return matrix

# Объявляем переменные
matrix_1 = Matrix(random_matrix(3, 3))
matrix_2 = Matrix(random_matrix(3, 3))

# Выводим матрицы и мумму матриц на экран
print('Первая матрица:')
print(matrix_1)
print('Вторая матрица:')
print(matrix_2)
print('Сумма матриц:')
print(matrix_1 + matrix_2)
