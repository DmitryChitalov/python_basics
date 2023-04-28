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

    template_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def __init__(self, matrix_list_1, matrix_list_2):
        self.matrix_list_1 = matrix_list_1
        self.matrix_list_2 = matrix_list_2

    def __str__(self):
        return str(
            '\n'.join([
                str('\t'.join([
                    str(self.template_matrix[a][b]) for b in range(len(self.template_matrix[a]))
                ])) for a in range(len(self.template_matrix))
            ])
        )

    def __add__(self):
        for a in range(len(self.matrix_list_1)):
            for b in range(len(self.matrix_list_2[a])):
                self.template_matrix[a][b] = self.matrix_list_1[a][b] + self.matrix_list_2[a][b]
        return self.__str__()


print(Matrix([[5, 18, 11], [6, 17, 23], [41, 30, 9]], [[5, 18, 11], [6, 17, 23], [41, 50, 9]]).__add__())
