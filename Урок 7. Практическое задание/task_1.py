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

    def __init__(self, params):
        self.values = params

    def __str__(self):
        line = ''
        for elem in self.values:
            line += ' '.join(map(str,elem)) + '\n'
        return line

    def __add__(self, other):
        try:
            result = []
            for i in range(len(self.values)):
                temp_element = []
                for j in range(len(self.values[i])):
                    temp_element.append(self.values[i][j] + other.values[i][j])
                result.append(temp_element)
        except IndexError:
            return "matrix are not the same size"
        except TypeError:
            return "can't make sum of different types"
        except:
            return "Unkonw error"
        return result


obj1 = Matrix([[6, 7, 8], [4, 5, 6]])
print(obj1)
print("_____")
obj2 = Matrix([[1, 2, 3], [4, 5, 6]])
print(obj2)
print("=====")
print(obj1 + obj2)