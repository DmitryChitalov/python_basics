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

class Cell:
    
    __quantity:int = 0
    _cell_name:str = None

    def __init__(self, quantity:int, cell_name:str) -> None:
        self.__quantity = quantity
        self._cell_name = cell_name
        print(f"Born cell with quantity {self.__quantity}")

    def __add__(self, obj) -> None:
        if issubclass(type(obj), Cell):
            cell:Cell = obj
            print(f"Cell {cell._cell_name} added to cell {self._cell_name}")
            self.quantity = self.quantity + cell.quantity
            cell.quantity = 0

    def __sub__(self, obj) -> None:
        if issubclass(type(obj), Cell):
            cell:Cell = obj
            print(f"Try subrtract cell {cell._cell_name} from cell {self._cell_name}")
            if self.quantity >= cell.quantity:
                print(f"Cell {cell._cell_name} subtracted from cell {self._cell_name}")
                self.quantity = self.quantity - cell.quantity
            else:
                print(f"Can't decrese cell quantity. Base quantity less than target on {cell.quantity - self.quantity}")

    def __mul__(self, obj):
        if issubclass(type(obj), Cell):
            cell:Cell = obj
            print(f"Multiplicate cell {self._cell_name} and {cell._cell_name}")
            result = Cell(self.quantity * cell.quantity, "cell_mull")
            self.quantity = 0
            cell.quantity = 0
            return result

    def __truediv__(self, obj):
        if issubclass(type(obj), Cell):
            cell:Cell = obj
            print(f"Divide cell {self._cell_name} on {cell._cell_name}")
            result = Cell(self.quantity // cell.quantity, "cell_truediv")
            self.quantity = 0
            cell.quantity = 0
            return result

    def make_order(self, count_per_row:int) -> str:
        result = ""
        ndx = 0
        ndx_r = 0
        while ndx < self.quantity:
            if ndx_r < count_per_row - 1:
                result += "*"
                ndx_r += 1
            else:
                ndx_r = 0
                result += "*\n"
            ndx += 1

        return result

    @property
    def quantity(self) -> int:
        return self.__quantity

    @quantity.setter
    def quantity(self, val:int) -> None:
        if val >= 0:
            self.__quantity = val
            if val == 0:
                print(f"Cell {self._cell_name} is dead, her quantity is 0")
            else:
                print(f"New cell {self._cell_name} quantity is {self.__quantity}")
        else:
            print(f"Cell quantity can't be less than 0")


cell_1 = Cell(10, "cell1")
cell_2 = Cell(20, "cell2")
cell_3 = Cell(5, "cell3")
cell_4 = Cell(7, "cell4")
cell_5 = Cell(12, "cell5")

cell_1 + cell_2
print()
cell_1 - cell_3
print()
cell:Cell = cell_1 / cell_4
print()
cell = cell * cell_5
print()

count_quantity_per_row = 5
print(f"Show struct cell {cell._cell_name} as {count_quantity_per_row} per row")
print(cell.make_order(count_quantity_per_row))