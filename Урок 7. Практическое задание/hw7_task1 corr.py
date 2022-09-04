class Matrix:
    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __str__(self):
        return '\n'.join(map(str, self.matrix_list))

    def __add__(self, other):
        for el in range(len(self.matrix_list)):
            for i in range(len(other.matrix_list[el])):
                self.matrix_list[el][i] = self.matrix_list[el][i] + other.matrix_list[el][i]
        return Matrix.__str__(self)


m = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"{m}\n")
print(f"{m2}\n")
print(m + m2)
