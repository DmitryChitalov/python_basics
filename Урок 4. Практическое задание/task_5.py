"""
5. Реализовать формирование списка, используя функцию range()
и возможности генераторного выражения.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать лямбда-функцию и функцию reduce().
"""

from functools import reduce

input_list = [elem for elem in range(100, 1001) if elem % 2 == 0]

result = reduce(lambda total, elem: total * elem, input_list)
print(f"Result: {result}")
