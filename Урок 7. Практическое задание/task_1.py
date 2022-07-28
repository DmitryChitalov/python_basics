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

    def __init__(self, value: list):
        self.value = value

    def __str__(self):
        return "\n".join(
            str(row).strip('[]').replace(',', '')
            for row in self.value
        )

    def __add__(self, other: 'Matrix'):
        rows_count = len(self.value)
        items_count = len(self.value[0])

        new_matrix = [
            [
                self.value[row][i] + other.value[row][i]
                for i in range(items_count)
            ]
            for row in range(rows_count)
        ]

        return Matrix(new_matrix)


mtx1 = Matrix([
    [1, 2, 3],
    [5, 6, 5],
    [2, 5, 8],
])

mtx2 = Matrix([
    [8, 6, 4],
    [3, 1, 1],
    [6, 3, 1],
])

summ = mtx1 + mtx2

print(f"Матрица 1:\n{mtx1}")
print(f"Матрица 2:\n{mtx2}")

print(f"Сумма матриц:\n{summ}")
