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
import copy


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        s = ''
        for i in range(len(self.matrix)):
            s = s + '\t'.join(map(str, self.matrix[i])) + '\n'
        return s

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix):
            raise ValueError('Матрицы разных размерностей нельзя сложить!')

        tmp = copy.deepcopy(self.matrix)
        for i in range(len(self.matrix)):
            for k in range(len(self.matrix[i])):
                tmp[i][k] = self.matrix[i][k] + other.matrix[i][k]
        return Matrix(tmp)


if __name__ == '__main__':
    lst_1 = [[1, 2, 4], [3, 4, 5], [5, 6, 6]]
    lst_2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    m_1 = Matrix(lst_1)
    m_2 = Matrix(lst_2)
    print(m_1)
    print(m_2)

    sum_result = m_1 + m_2

    print(sum_result)
