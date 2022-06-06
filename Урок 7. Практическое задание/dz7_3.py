# Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
# вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное
# (с округлением до целого) деление клеток, соответственно. Сложение. Объединение двух клеток.
# При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток
# больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как произведение
# количества ячеек этих двух клеток.
# Деление. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление
# количества ячеек этих двух клеток.

class Cell():
    def __init__(self, size):
        self.size = size

    def __str__(self):
        return "Ячейка(size:{})".format(self.size)

    # Перегружаем оператор +
    def __add__(self, other):
        return Cell(self.size + other.size)

    # Перегружаем оператор -
    def __sub__(self, other):
        new_size = self.size - other.size
        if new_size > 0:
            return Cell(new_size)
        else:
            raise ArithmeticError(new_size)

    # Перегружаем оператор *
    def __mul__(self, other):
        return Cell(self.size * other.size)

    # Перегружаем оператор *
    def __truediv__(self, other):
        return Cell(self.size // other.size)

    # string representation
    def make_order(self, rowsize):
        residual = self.size
        strres = ''
        while residual:
            thisrowsize = rowsize if residual >= rowsize else residual
            strres += '*' * thisrowsize
            residual -= thisrowsize
        return strres


c5 = Cell(5)
c6 = Cell(6)

print('сложение: c5 + c6:', c5 + c6)

print('вычитание: c6 - c5:', c6 - c5)

try:
    print(c5 - c6)
except ArithmeticError:
    print('вычитание: c5 - c6: Неверные аргументы')

print('умножение: c5 * c6:', c5 * c6)

print('деление: c5 / c6:', c5 / c6)

print('деление: c6 / c5:', c6 / c5)
