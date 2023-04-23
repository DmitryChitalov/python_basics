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
    def __init__(self, *args):
        self.my_list = list(args)

    def __str__(self):
        matrix = ''
        for i in range(len(self.my_list)):
            matrix += ' '.join(map(str, self.my_list[i])) + '\n'
        return matrix

    def __add__(self, other):
        matrix_1 = self.my_list
        new_matrix = ''
        for i in range(len(self.my_list)):
            for el in range(len(self.my_list[i])):
                matrix_1[i][el] = self.my_list[i][el] + other.my_list[i][el]
            new_matrix += ' '.join(map(str, self.my_list[i])) + '\n'
        return new_matrix


m_1 = Matrix([0, 1, 2], [3, 4, 5], [6, 7, 8])
print(m_1)
m_2 = Matrix([9, 8, 7], [6, 5, 4], [3, 2, 1])
print(m_2)
print(m_1 + m_2)
