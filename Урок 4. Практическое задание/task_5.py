"""
5. Реализовать формирование списка, используя функцию range()
и возможности генераторного выражения.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать лямбда-функцию и функцию reduce().
"""
from functools import reduce
from math import prod

user_lisr = [i for i in range(100, 1001) if i % 2 == 0]

my_func = lambda a, b: a * b

result = prod(user_lisr)

print(reduce(my_func, user_lisr))
print(result)
