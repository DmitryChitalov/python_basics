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

# pylint: disable=missing-class-docstring,pointless-string-statement,consider-using-enumerate


class Matrix:
    def __init__(self, *args):
        self.new_lst = list(args)

    def __str__(self):
        result = '\n'.join(map(str, self.new_lst))
        '''result -> [1, 2, 3]
                     [4, 5, 6]
                     [7, 8, 9]'''
        result = result.replace(',', '').replace('[', '').replace(']', '')
        '''result -> 1 2 3
                     4 5 6
                     7 8 9'''
        return result

    def __add__(self, other):
        new_sum = []
        line_sum = []
        for x in range(len(self.new_lst)):
            for y in range(len(self.new_lst[x])):
                line_sum.append(self.new_lst[x][y] + other.new_lst[x][y])
            new_sum.append(line_sum)
            line_sum = []
        return Matrix('\n'.join(map(str, new_sum)))


matrix_1 = Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
print(matrix_1)
print()

matrix_2 = Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
print(matrix_2)
print()

print(f'Сумма матриц:\n{matrix_1 + matrix_2}')
