"""
5. Реализовать формирование списка, используя функцию range()
и возможности генераторного выражения.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать лямбда-функцию и функцию reduce().
"""

from functools import reduce

my_list = [a for a in range(100, 1001, 2)]
my_func = reduce(lambda b, b1: b * b1, my_list)
print(my_func)
