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
    def __init__(self, content):
        self.content = content

    def __str__(self):
        return '\n'.join([' '.join(['%d' % el for el in row]) for row in self.content])

    def __add__(self, other):
        __result = []
        __string_result = []
        for row_num in range(len([row for row in self.content])):
            for el_num in range(len([el for el in self.content[row_num]])):
                __string_result.append(self.content[row_num][el_num] + other.content[row_num][el_num])
            __result.append(__string_result)
            __string_result = []
        return Matrix(__result)


My_Matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [6, 5, 4]])
My_Matrix2 = Matrix([[9, 8, 8], [8, 7, 7], [7, 6, 6], [4, 5, 6]])
print("Первая матрица:")
print(My_Matrix)
print("Вторая матрица:")
print(My_Matrix2)
print("Сумма матриц:")
print(My_Matrix + My_Matrix2)
