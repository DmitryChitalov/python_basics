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
    def __init__(self, matr):
        self.matr = matr

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.matr]))

    def __add__(self, other):
        new_matr = []
        for i in range(len(self.matr)):
            new_line = []
            for j in range(len(self.matr[i])):
                new_line.append(self.matr[i][j] + other.matr[i][j])
            new_matr.append(new_line)
        return Matrix(new_matr)

matr1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matr1)
matr2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matr2)
my_matr = matr1 + matr2
print(my_matr)
