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

from sys import argv


class Matrix:
    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        return f'{self.lists}'

    def __add__(self, other):
        result = []
        for i in self.lists:
            for j in other.lists:
                if self.lists.index(i) == other.lists.index(j):
                    temp_list = []
                    for elem1 in i:
                        for elem2 in j:
                            if i.index(elem1) == j.index(elem2):
                                temp_list.append(elem1 + elem2)
                    if len(i) > len(j):
                        for appender in i[-(len(i) - len(j)):]:
                            temp_list.append(appender)
                    elif len(j) > len(i):
                        for appender in j[-(len(j) - len(i)):]:
                            temp_list.append(appender)
                    result.append(temp_list)
        if len(self.lists) > len(other.lists):
            for appender in self.lists[-(len(self.lists) - len(other.lists)):]:
                result.append(appender)

        if len(other.lists) > len(self.lists):
            for appender in other.lists[-(len(other.lists) - len(self.lists)):]:
                result.append(appender)
        return Matrix(result)


a = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
c = Matrix([[1, 2, 3, 4], [5, 6, 7, 8]])
d = Matrix([[1, 2, 3, 4, 5], [5, 6, 7, 8, 9], [4, 5, 6], [7, 8, 9]])

print(a)
print(a + b)
print(a + c)
print(a + d)
