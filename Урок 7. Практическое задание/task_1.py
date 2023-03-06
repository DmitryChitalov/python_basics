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
    def __init__(self, die):
        self.die = die
        self.new_die = ''

    def __str__(self):

        for k in range(len(self.die)):
            if len(self.new_die) != 0:
                self.new_die += '\n'
            for t in self.die[k]:
                self.new_die += f'{str(t)} '
        return self.new_die

    def __add__(self, other):
        if len(self.die) == len(other.die):
            for k in range(len(self.die)):
                for j in range(len(other.die[0])):
                    self.die[k][j] = self.die[k][j] + other.die[k][j]
            return Matrix(self.die)
        else:
            return 'Матрицы должны быть одного размера'


die = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(f'Сложение матриц:')
new_die = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
new_die_update = Matrix([[1, 2, 3], [2, 3, 4], [5, 6, 7]])
print(new_die + new_die_update)
