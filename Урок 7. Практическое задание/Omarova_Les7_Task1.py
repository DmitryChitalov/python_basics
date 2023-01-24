------
1.Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
------

class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        for row in self.my_list:
            for i in row:
                print(f"{i:4}", end="")
            print()
        return ''

    '''2 варианта реализации __str__'''

    # def __str__(self):
    #     return '\n'.join(map(str, self.my_list))

    # def __str__(self):
    #     return str('\n'.join(['\t'.join([str(el) for el in i]) for i in self.my_list]))

    def __add__(self, other):
        for i in range(len(self.my_list)):
            for i_2 in range(len(other.my_list[i])):
                self.my_list[i][i_2] = self.my_list[i][i_2] + other.my_list[i][i_2]
        return Matrix.__str__(self)


m = Matrix([[-1, 0, 1], [-1, 0, 1], [0, 1, -1], [1, 1, -1]])
new_m = Matrix([[-2, 0, 2], [-2, 0, 2], [0, 2, -2], [2, 2, -7]])
print(m.__add__(new_m))