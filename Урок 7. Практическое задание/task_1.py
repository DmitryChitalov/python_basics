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
    def __init__(self, data):
        self.data = data

    def __str__(self):
        result = ''
        for row in self.data:
            result += ' '.join([str(elem) for elem in row]) + '\n'
        return result

    def __add__(self, other):
        if len(self.data) != len(other.data):
            raise ValueError('Матрицы разной размерности')
        result = []
        for i in range(len(self.data)):
            if len(self.data[i]) != len(other.data[i]):
                raise ValueError('Матрицы разной размерности')
            row = []
            for j in range(len(self.data[i])):
                row.append(self.data[i][j] + other.data[i][j])
            result.append(row)
        return Matrix(result)


m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(m1)
print(m2)

m_sum = m1 + m2

print(m_sum)
