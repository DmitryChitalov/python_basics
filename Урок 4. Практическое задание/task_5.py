"""
5. Реализовать формирование списка, используя функцию range()
и возможности генераторного выражения.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать лямбда-функцию и функцию reduce().
"""
from functools import reduce

nums = [num for num in range(100, 1000 + 1) if num % 2 == 0]
func_lmd = (lambda number_1, number_2: number_1 * number_2)
result = reduce(func_lmd, nums)
print(result)
