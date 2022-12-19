class Matrix:

    def __init__(self, *args):
        self.my_matrix = list(args)

    def __str__(self):
        result = ""
        for el in self.my_matrix:
             for i in range(len(el) - 1):
                 result += str(el[i]) + " "
             result += str(el[i + 1]) + "\n"
        return result

    def __add__(self, other):
        buffer = []
        result = []
        for el in range(len(self.my_matrix)):
            for i in range(len(self.my_matrix[el])):
                buffer.append(self.my_matrix[el][i] + other.my_matrix[el][i])
            result.append(buffer)
            buffer = []
        return Matrix(*result)

a = Matrix([4, 3, 4], [3, 2, 8], [9, 3, 8])
b = Matrix([2, 7, 10], [32, 24, 68], [39, 32, 38])
print(a)
print(b)
print(a + b)
