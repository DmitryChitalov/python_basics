"""
5. Реализовать формирование списка, используя функцию range()
и возможности генераторного выражения.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать лямбда-функцию и функцию reduce().
"""
from functools import reduce

my_list = [el for el in range(100, 1000) if el % 2 == 0]
print(reduce(lambda arg1, arg2: arg1 * arg2, my_list))
