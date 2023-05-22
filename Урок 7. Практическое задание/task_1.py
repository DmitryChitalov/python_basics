class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        for row in self.my_list:
            for j in row:
                print(f"{j:5}", end="")
            print()
        return ''


    def __add__(self, other):
        for j in range(len(self.my_list)):
            for i in range(len(other.my_list[j])):
                self.my_list[j][i] = self.my_list[j][i] + other.my_list[j][i]
        return Matrix.__str__(self)

        m = Matrix([[-1, 20], [36, 40], [51, -1]])
        new_m = Matrix([[32, 2], [1, 3], [0, 87]])
        print(m + new_m)

        m = Matrix([[-1, 0, 31], [-1, 4, 4], [0, 60, -1]])
        new_m = Matrix([[4, 5, 1], [3, 0, 2] [-1, 4, -7]])
        print(m + new_m)

        m = Matrix([[-1, 5, 5, 1], [10, 0, 5, 0]])
        new_m = Matrix([[4, 0, 3, 2], [-2, 3, 2, 1]])
        print(m + new_m)