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

    def __init__(self, list_values):
        self.list_values = list_values

    def __str__(self):
        print_result = ''
        for i in range(0, len(self.list_values)):
            print_result += f'{self.list_values[i]} \n'
        return print_result

    def __add__(self, other):
        if (len(self.list_values) == len(other.list_values)) \
                and (len(self.list_values[0]) == len(other.list_values[0])):
            result = []
            for i in range(0, len(self.list_values)):
                row = []
                for j in range(0, len(self.list_values[0])):
                    row.append(self.list_values[i][j] + other.list_values[i][j])
                result.append(row)
            return Matrix(result)
        else:
            return f'Error! You summarize matrices of different dimensions'


m = Matrix([[3], [3]])
k = Matrix([[2, 3], [3, 4]])
l = Matrix([[2, 3], [3, 4]])
print(m)
print(m + k)
print(k + l)