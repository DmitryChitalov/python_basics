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
    def __init__(self, ls:list):
        self.ls = ls
    def __str__(self):
        result = []
        for row in self.ls:
            result.append(' '.join([str(k) for k in row]))
        return '\n'.join(result)
    def __add__(self, other):
        if len(self.ls) == len(other.ls):
            result = []
            for i, row in enumerate(self.ls):
                new_list = list(map(lambda x, y: x + y, row, other.ls[i]))
                result.append(new_list)
            return Matrix(result)
        else:
            return
list_lists_1 = [[1, 2, 3], [3, 3, 3], [4, 3, 2]]
list_lists_2 = [[2, 5, 5], [4, 3, 3], [1, 1, 2]]
m1 = Matrix(list_lists_1)
m2 = Matrix(list_lists_2)
m3 = m1 + m2
print(f"Матрица 1:\n", m1, end='\n\n')
print(f"Матрица 2:\n", m2, end='\n\n')
print(f"Матрица 1 + Матрица 2:\n", m3)
