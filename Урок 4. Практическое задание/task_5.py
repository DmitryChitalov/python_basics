"""
5. Реализовать формирование списка, используя функцию range()
и возможности генераторного выражения.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать лямбда-функцию и функцию reduce().
"""

from functools import reduce

def my_num(num_1, num_2):
    return num_1 * num_2

my_list = [num_2 for num_2 in range(100, 1001, 2)]
otv_1 = reduce(my_num, my_list)

print(f'Список из четных чисел: {my_list}')
print(f'Ответ перемножения всех элементов списка: {otv_1}')