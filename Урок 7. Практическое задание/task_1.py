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
        self.nw_list = list(args)
    def __str__(self):
        result = '\n'.join(map(str, self.nw_list))
        result = result.replace(',', '').replace('[', '').replace(']', '')
        return result
    def __add__(self, other):
        new_sum = []
        other_sum = []
        for i in range(len(self.nw_list)):
            for j in range(len(self.nw_list[i])):
                other_sum.append((self.nw_list[i][j] + other.nw_list[i][j]))
            new_sum.append(other_sum)
            other_sum = []
        return Matrix('\n'.join((map(str, new_sum))))


a = Matrix([1,2,4], [1,5,6], [5, 6, 7])
b = Matrix([1,3,4], [5,6,6], [7, 7, 7])

print(a + b)

