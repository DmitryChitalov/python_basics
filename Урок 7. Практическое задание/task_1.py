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
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        result = ''
        for n in range(len(self.matrix)):
            for m in range(len(self.matrix[n])):
                result += str(self.matrix[n][m]) + ' '
            result += '\n'
        return result

    def __add__(self, other):
        for n in range(len(self.matrix)):
            for m in range(len(self.matrix)):
                self.matrix[n][m] = int(self.matrix[n][m]) + int(other.matrix[n][m])
        return Matrix(self.matrix)


my_source_matrix = []
for n in range(3):
    my_source_matrix.append(input('Введите три числа через запятую: ').split(','))

my_matrix = Matrix(my_source_matrix)
print(my_matrix)
my_matrix_2 = my_matrix
print(my_matrix + my_matrix_2)
