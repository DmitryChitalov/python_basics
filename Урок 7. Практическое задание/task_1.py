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
        self.new_str = m_list

    def __str__(self):
        z = ''
        for v in range(len(self.new_str)):
            z = z + '\t'.join(map(str, self.new_str[v])) + '\n'
        return z

    def __add__(self, other):
        if len(self.new_str) != len(other.new_str):
            return None
        add = self.new_str
        for v in range(len(self.new_str)):
            for k in range(len(self.new_str[v])):
                add[v][k] = self.new_str[v][k] + other.new_str[v][k]
        return Matrix(add)

fsum = Matrix([[10, 20, 15], [35, 30, 25], [40, 45, 50]])
secsum = Matrix([[-5, -10, 0], [20, -15, 25], [30, 45, 50]])

print(fsum)
print()
print(secsum)
print()
print(f'Сумма матриц:\n{fsum + secsum}')
