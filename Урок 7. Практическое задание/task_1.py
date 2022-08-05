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
    def __init__(self, lst):
        self.lst = lst

    def __str__(self):
        new_view = [str(el).strip('[]').replace(',', '')
                    for el in self.lst]
        return "\n".join(new_view)

    def __add__(self, other):
        try:
            for n in range(len(self.lst)):
                for m in range(len(self.lst)):
                    self.lst[n][m] = int(self.lst[n][m]) + int(other.lst[n][m])
            return Matrix(self.lst)
        except IndexError:
            print("Матрицы разного размера")
            exit(1)
        return None


a = Matrix([[1, 2, 3],[4, 5, 6],[22, 8, 45]])

b = Matrix([[1, 2, 3],[44, 29, 6],[7, 8, 9]])

print(f"Значения матрицы а:\n{a}")
print(f"Значения матрицы b:\n{b}")

c = a + b
print(f"Сумма матриц а и b:\n{c}")
