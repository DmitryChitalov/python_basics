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
    new_matrix = {'m': []}

    def __init__(self, matrix_list):
        self.matrix = matrix_list

    def __add__(self, other):
        self.new_matrix['m'] = [[a+b for a, b in zip(i[0], i[1])] for i in zip(self.matrix, other.matrix)]
        return self.__str__(self.new_matrix['m'])

    def __str__(self, m=None):
        if not m:
            return '\n'.join([' '.join(map(str, i)) for i in self.matrix])
        else:
            return '\n'.join([' '.join(map(str, i)) for i in m])


matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(f"Пример:\n{matrix_1}\n\n{matrix_2}\n")
print(f"Сумма матриц:\n{matrix_1 + matrix_2}\n")

print(f"Новая общая матрица:\n{matrix_1.new_matrix['m']}\n{matrix_2.new_matrix['m']}")
