"""
5. Реализовать формирование списка, используя функцию range()
и возможности генераторного выражения.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать лямбда-функцию и функцию reduce().
"""
#!/usr/bin/env python3
from functools import reduce

initial_list = [i for i in range(100, 1001, 2)]
result = reduce((lambda x, y: x * y), initial_list)
print(result)
# print(len(initial_list)) ### должно быть 451, если включать в список 100 и 1000

# def checking_calculation(initial_list):
#     func_result = 1
#     for i in initial_list:
#         func_result = func_result * i
#     return func_result

# print(checking_calculation(initial_list))
