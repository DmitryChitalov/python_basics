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
        self.n_list = list(args)

    def __str__(self):
        res = '\n'.join(map(str, self.n_list))
        result = res.replace(',', '').replace('[', '').replace(']', '')
        return result

    def __add__(self, other):
        n_sum = []
        l_sum = []
        for x in range(len(self.n_list)):
            for y in range(len(self.n_list[x])):
                l_sum.append(self.n_list[x][y] + other.n_list[x][y])
            n_sum.append(l_sum)
            l_sum = []
        return Matrix('\n'.join(map(str, n_sum)))

M_Obj_1 = Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
print(M_Obj_1)
print()

M_Obj_2 = Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
print(M_Obj_2)
print()

print(f'{M_Obj_1 + M_Obj_2}')
print()