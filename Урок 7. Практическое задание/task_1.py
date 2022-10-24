'''
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
'''


class Matrix:
    def __init__(self, lists):
        self.matrix = lists

    def __str__(self):
        string = ''
        for el in self.matrix:
            string = f'{string}{"  ".join(map(str, el))}\n'
        return string

    def __add__(self, other):
        res = []
        num = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                sum_matrix = other.matrix[i][j] + self.matrix[i][j]
                num.append(sum_matrix)
                if len(num) == len(self.matrix[0]):
                    res.append(num)
                    num = []
        return Matrix(res)


lst1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lst2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix1 = Matrix(lst1)
matrix2 = Matrix(lst2)

print('\nМатрица 1: ')
print(matrix1.__str__())

print('Матрица 2: ')
print(matrix2.__str__())

print('Сумма матриц: ')
print(matrix1 + matrix2)

input('\nНажмите Enter...')
