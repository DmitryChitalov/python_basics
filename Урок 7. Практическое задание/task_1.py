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
    def __init__(self, *args):
        self.list_m = list(args)

    def __str__(self):
        make_m = '\n'.join(map(str, self.list_m))
        make_m = make_m.replace(',', '').replace('[', '').replace(']', '')
        return make_m

    def __add__(self, other):
        sum_sum = []
        sum_row = []
        for x in range(len(self.list_m)):
            for y in range(len(self.list_m[x])):
                sum_row.append(self.list_m[x][y] + other.list_m[x][y])
            sum_sum.append(sum_row)
            sum_row = []
        return Matrix('\n'.join(map(str, sum_sum)))


matrix_1 = Matrix([1, 31, 22], [5, 37, 43], [10, 51, 86])
print(f'{matrix_1}\n')
matrix_2 = Matrix([3, 5, 32], [2, 4, 6], [-1, 64, -8])
print(f'{matrix_2}\n')
print(f'Сложение матриц:\n{matrix_1 + matrix_2}')
