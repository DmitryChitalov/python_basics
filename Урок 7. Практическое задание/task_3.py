"""
Задание 3.

Реализовать программу работы с органическими клетками, состоящими из ячеек.

Необходимо создать класс Клетка (Cell).

В его конструкторе инициализировать параметр (quantity),
соответствующий количеству ячеек клетки (целое число).

В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (add()),
вычитание (sub()),
умножение (mul()),
деление (truediv()).

Данные методы должны применяться только к клеткам и выполнять увеличение,
уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.

Сложение. Объединение двух клеток.
При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.

Вычитание. Участвуют две клетки.
Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
иначе выводить соответствующее сообщение.

Умножение. Создается общая клетка из двух.
Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.

Деление. Создается общая клетка из двух.
Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.


** - По желанию: В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и
количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****...,
где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.

Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n*****.
Подсказка: подробный список операторов для перегрузки доступен по ссылке.

------------------------------------------------------------------------------
Пример клиентского кода:
print("Создаем объекты клеток")
cell1 = Cell(30)
cell2 = Cell(25)

cell3 = Cell(10)
cell4 = Cell(15)

print()

print("Складываем")
print(cell1 + cell2)

print()

print("Вычитаем")
print(cell2 - cell1)
print(cell4 - cell3)

print()

print("Умножаем")
print(cell2 * cell1)

print()

print("Делим")
print(cell1 / cell2)

print()

print("Организация ячеек по рядам")
print(cell1.make_order(5))
print(cell2.make_order(10))

------------------------------------------------------------------------------
Результаты:
Создаем объекты клеток

Складываем
Сумма клеток = (55)

Вычитаем
Разность отрицательна, поэтому операция не выполняется
Разность клеток = (5)

Умножаем
Умножение клеток = (750)

Делим
Деление клеток = (1)

Организация ячеек по рядам
*****\n *****\n *****\n *****\n *****\n *****\n
**********\n **********\n *****
"""


def raise_type_error_if_needed(other, message):
    if not isinstance(other, Cell):
        raise TypeError(message)


def exception_decorator(func):
    def some_function(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except BaseException as err:
            return f"Unexpected {err=}, {type(err)=}"
    return some_function


class Cell:
    quantity: int

    def __init__(self, quantity: int):
        self.quantity = quantity

    def __str__(self):
        return f'Quantity: {self.quantity}'

    def __add__(self, other):
        raise_type_error_if_needed(other, 'Cannot add cell and non-cell types')
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        raise_type_error_if_needed(other, 'Cannot subtract cell and non-cell types')
        sub_result = self.quantity - other.quantity
        if sub_result > 0:
            return Cell(sub_result)
        raise ValueError(f'Cell quantity cannot be negative (result={sub_result})')

    def __mul__(self, other):
        raise_type_error_if_needed(other, 'Cannot multiply cell and non-cell types')
        return Cell(self.quantity * other.quantity)

    def __truediv__(self, other):
        raise_type_error_if_needed(other, 'Cannot divide cell and non-cell types')
        return Cell(self.quantity // other.quantity)

    def make_order(self, cells_in_row):
        row = ''
        for _ in range(self.quantity // cells_in_row):
            row += f'{"*" * cells_in_row} \\n'
        row += f'{"*" * (self.quantity % cells_in_row)}'
        return row


cells1 = Cell(40)
cells2 = Cell(10)
print(f'cells1: {cells1}')
print(f'cells2: {cells2}')
print(f'cells1 + cells2: {cells1 + cells2}')
print(f'cells1 - cells2: {cells1 - cells2}')

my_dec = exception_decorator(cells1.__add__)
print(f'cells1 + 4: {my_dec(22)}')

my_dec = exception_decorator(cells2.__sub__)
print(f'cells2 - cells1: {my_dec(cells1)}')

print(f'cells1 * cells2: {cells1 * cells2}')
print(f'cells1 / cells2: {cells1 / cells2}')

print(f'cells2.make_order(6): {cells2.make_order(6)}')
print(f'cells1.make_order(12): {cells1.make_order(12)}')
