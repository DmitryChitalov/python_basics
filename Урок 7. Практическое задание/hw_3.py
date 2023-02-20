class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return f'({self.quantity})'

    def __add__(self, other):
        return f'Сумма клеток = {(Cell(self.quantity + other.quantity))}'

    def __sub__(self, other):
        if (self.quantity - other.quantity) > 0:
            return f'Разность клеток = {Cell(int(self.quantity - other.quantity))}'
        return f'Разность отрицательна, поэтому операция не выполняется'

    def __mul__(self, other):
        return f'Умножение клеток = {Cell(int(self.quantity * other.quantity))}'

    def __truediv__(self, other):
        return f'Деление клеток = {Cell(round(self.quantity // other.quantity))}'

    def make_order(self, cells_count):
        row = ''
        for _ in range(int(self.quantity / cells_count)):
            row += f'{"*" * cells_count}\\n '
        row += f'{"*" * (self.quantity % cells_count)}'
        return row


print('Создаем объекты клеток')
cell1 = Cell(30)
cell2 = Cell(25)

cell3 = Cell(10)
cell4 = Cell(15)

print()

print('Складываем')
print(cell1 + cell2)

print()

print('Вычитаем')
print(cell2 - cell1)
print(cell4 - cell3)

print()

print('Умножаем')
print(cell1 * cell2)

print()

print('Делим')
print(cell1 // cell2)

