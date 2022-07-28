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
    def __init__(self, m_list):
        self.m_list = m_list

    def __str__(self):
        for row in self.m_list:
            for i in row:
                print(f"{i:4}", end="")
            print()
        return ''

    def __str__(self):
        return '\n'.join(map(str, self.m_list))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(el) for el in i]) for i in self.m_list]))

    def __add__(self, other):
        for i in range(len(self.m_list)):
            for i_2 in range(len(other.m_list[i])):
                self.m_list[i][i_2] = self.m_list[i][i_2] + other.m_list[i][i_2]
        return Matrix.__str__(self)


m = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m_new = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"Сумма матрицы\n{m.__add__(m_new)}")
