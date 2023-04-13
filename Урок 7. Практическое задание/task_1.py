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

#1 
class Matrix:
    def __init__(self, list_1, list_2):

        self.list_1 = list_1
        self.list_2 = list_2

        list_1 = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]

        list_2 = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]

        result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        for i in range(len(list_1)):
            for j in range(len(list_1[0])):
                result[i][j] = list_1[i][j] + list_2[i][j]
                print(result)
                
    
#2

class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        for row in self.my_list:
            for i in row:
                print(f"{i:4}", end="")
            print()
        return ''

    def __add__(self, other):
        for i in range(len(self.my_list)):
            for i_2 in range(len(other.my_list[i])):
                self.my_list[i][i_2] = self.my_list[i][i_2] + other.my_list[i][i_2]
        return Matrix.__str__(self)


m = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
new_m = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(m.__add__(new_m))

