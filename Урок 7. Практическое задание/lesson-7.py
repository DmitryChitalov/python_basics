"""
Задание 1.
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init()__),
который должен принимать данные (список списков) для формирования матрицы.
[[], [], []]
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции
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


# в условии указан размер матрицы, поэтому этот способ применим.
# для незаданного заранее размера (или матриц большого размера) данный способ нецелесообразен
class Matrix:

    def __init__(self, param1, param2, param3):
        self.param_list1 = list(param1)
        self.param_list2 = list(param2)
        self.param_list3 = list(param3)

    def __add__(self, other):
        self.rezult_list1 = []
        self.rezult_list2 = []
        self.rezult_list3 = []
        for i in range(len(self.param_list1)):
            self.rezult_list1.append(self.param_list1[i] + other.param_list1[i])

        for i in range(len(self.param_list2)):
            self.rezult_list2.append(self.param_list2[i] + other.param_list2[i])

        for i in range(len(self.param_list3)):
            self.rezult_list3.append(self.param_list3[i] + other.param_list3[i])

        return f"Сумма матриц: \n{self.rezult_list1} \n{self.rezult_list2} \n{self.rezult_list3}\n ".replace(',',
                                                                                                             '').replace(
            '[', '').replace(']', '')

    def __str__(self):
        return f"{self.param_list1} \n{self.param_list2} \n{self.param_list3}\n ".replace(',', '').replace('[',
                                                                                                           '').replace(
            ']', '')


matr_1 = Matrix([1, 2, 3], [1, 2, 3], [1, 2, 3])
matr_2 = Matrix([3, 2, 3], [2, 2, 3], [1, 2, 1])
print(matr_1)
print(matr_2)
print(matr_2 + matr_1)

"""
Задание 2.
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Единственный класс этого проекта — одежда (класс Clothes).
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: v и h, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (v/6.5 + 0.5),
для костюма (2*h + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать
абстрактный класс для единственного класса проекта,
проверить на практике работу декоратора @property
Пример:
Расход ткани на пальто = 1.27
Расход ткани на костюм = 20.30
Общий расход ткани = 21.57
Два класса: абстрактный и Clothes
"""
from abc import ABC, abstractmethod


class Abstract(ABC):
    def result_for_coat(self):
        pass

    def result_for_suit(self):
        pass


class Clothes(Abstract):
    def __init__(self):
        self.size = int(input("Если Вы шьете пальто, введите размер"))
        self.height = float(input("Если Вы шьете костюм, введите рост"))

    @property
    def result_for_coat(self):
        return f"На пальто требуется {self.size / 6.5 + 0.5} ткани"

    @property
    def result_for_suit(self):
        return f"На пальто требуется {2 * self.height + 0.3} ткани"

    @property
    def result_for_all(self):
        return f"Общий расход ткани {(self.size / 6.5 + 0.5) + (2 * self.height + 0.3)} "


el = Clothes()
print(el.result_for_coat)
print(el.result_for_suit)
print(el.result_for_all)
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
"""


class Cell:
    def __init__(self, quantity):
        self.quantity = quantity

    def __str__(self):
        return f'{self.quantity}'

    def __add__(self, other):
        return f"Результат сложения клеток {str(Cell(self.quantity + other.quantity))}"

    def __sub__(self, other):
        if (self.quantity - other.quantity > 0):
            return f"Результат вычитания клеток {str(Cell(self.quantity - other.quantity))}"
        else:
            print("Невозможная операция")

    def __mul__(self, other):
        return f"Результат умножения клеток {str(Cell(self.quantity * other.quantity))}"

    def __truediv__(self, other):
        if (self.quantity / other.quantity > 1):
            return f"Результат деления клеток {str(Cell(self.quantity // other.quantity))}"
        else:
            return f"Осторожно! в результате  деления клеток у Вас пропала клетка! Результат деления =  {str(Cell(self.quantity // other.quantity))}"


cell1 = Cell(int(input("Введите количество ячеек клетки")))
cell2 = Cell(int(input("Введите количество ячеек клетки")))

print(cell1 + cell2)
print(cell1 - cell2)
print(cell1 * cell2)
print(cell1 / cell2)
