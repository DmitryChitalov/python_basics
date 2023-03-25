"""
5. Реализовать формирование списка, используя функцию range()
и возможности генераторного выражения.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать лямбда-функцию и функцию reduce().
"""

from functools import reduce

def multiply(list):
    return reduce(lambda product, item: product * item, list)

source_list = [item for item in range(100, 1001, 2)]
print("source list:", source_list)
print("product of numbers in list =", multiply(source_list))
