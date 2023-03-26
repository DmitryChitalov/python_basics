"""
5. Реализовать формирование списка, используя функцию range()
и возможности генераторного выражения.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать лямбда-функцию и функцию reduce().
"""
from functools import reduce
multiplication = lambda res, multiplicator: res * multiplicator

list_by_range = [el for el in range(100, 1001, 2)]
print(reduce(multiplication, list_by_range))