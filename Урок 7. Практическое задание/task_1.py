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

"""
Выполенине! Емельяненко А.А.
"""


class Matrix:
    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        return f'{self.lists[0]:3} {self.lists[1]:3} {self.lists[2]:3}\n' \
               f'{self.lists[3]:3} {self.lists[4]:3} {self.lists[5]:3}'

    def __add__(self, next_matrix):
        self.lists = [sum(el) for el in zip(self.lists, next_matrix.lists)]
        return self.__str__()


matrix = Matrix([1, 2, 3, 4, 5, 6])
matrix2 = Matrix([5, 5, 5, 5, 5, 5])

print(matrix, matrix2, sep='\n' * 2, end='\n' * 3)

print(matrix + matrix2)

# Альтернативное решение:

class Matrix:
    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        return f'{self.lists[0]:3} {self.lists[1]:3} {self.lists[2]:3}\n' \
               f'{self.lists[3]:3} {self.lists[4]:3} {self.lists[5]:3}'

    def __add__(self, next_matrix):
        self.lists = [sum(el) for el in zip(self.lists, next_matrix.lists)]
        return self.__str__()


matrix = Matrix([1, 2, 3, 4, 5, 6])
matrix2 = Matrix([5, 5, 5, 5, 5, 5])
matrix3 = Matrix([6, 6, 6, 6, 6, 7])

print(matrix, matrix2, sep='\n' * 2, end='\n' * 3, )

print(matrix + matrix2)
print(matrix3)
