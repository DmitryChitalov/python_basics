class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        if isinstance(other, Cell):
            return self.quantity + other.quantity

    def __sub__(self, other):
        if isinstance(other, Cell) and self.quantity - other.quantity > 0:
            return self.quantity - other.quantity

    def __truediv__(self, other):
        if isinstance(other, Cell):
            return self.quantity // other.quantity

    def __mul__(self, other):
        if isinstance(other, Cell):
            return self.quantity * other.quantity

    def make_order(self, row):
        result = ''
        for i in range(int(self.quantity / row)):
            result += '*' * row + '\n'
        result += '*' * (self.quantity % row) + '\n'
        return result

cell_1 = Cell(36)
cell_2 = Cell(5)

print('Сложение:', cell_1 + cell_2)
print('Вычитание:', cell_1 - cell_2)
print('Умножение:', cell_1 * cell_2)
print('Деление:', cell_1 / cell_2)
print('')
print(cell_1.make_order(10))
