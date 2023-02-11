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
    def __init__(self, matrix_of_list):
        self.matrix_of_list = matrix_of_list

    def __add__(self, other):
        my_list_3 = []
        for i in range(0, len(self.matrix_of_list)):
            my_list_4 = []
            for j in range(0, len(self.matrix_of_list[0])):
                my_list_4.append(self.matrix_of_list[i][j] + other.matrix_of_list[i][j])
            my_list_3.append(my_list_4)
        self.matrix_of_list = my_list_3
        return Matrix(self.matrix_of_list)

    def __str__(self):
        for i in self.matrix_of_list:
            for j in i:
               print(j, end=" ")
            print()
        return ""


matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix_1)
print(matrix_2)
matrix_3 = matrix_1 + matrix_2
print(matrix_3)
