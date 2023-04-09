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

    def __init__(self, list_1):
        self.list_1 = list_1

    def print_all_result(self):
        print(self.list_1)

    def __add__(self, other):

        sum_matrix = []
        for i in range(len(self.list_1)):
            for a in range(len(self.list_1[i])):
                sum_matrix.append(self.list_1[i][a] + other.list_1[i][a])
        new_list = [sum_matrix[i:i + 3] for i in range(0, len(sum_matrix), 3)]
        return Matrix(new_list)

    def __str__(self):
        empty_str_1 = ""
        for i in self.list_1:
            b = [str(el) for el in i]
            empty_str_1 += f'{" ".join(b)}\n'

        return f'{empty_str_1}\n'


obj = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
obj_2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(obj)
print(obj_2)
obj_3 = obj + obj_2
print(obj_3)
