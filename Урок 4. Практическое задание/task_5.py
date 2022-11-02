"""
5. Реализовать формирование списка, используя функцию range()
и возможности генераторного выражения.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать лямбда-функцию и функцию reduce().
"""


from functools import reduce

# Тест
test_count = reduce(lambda var_1, var_2: var_1 * var_2, [10, 3, 3])
print(test_count)
#


my_list = [x for x in range(100, 1001) if x % 2 == 0]
print(my_list)

final_count = reduce(lambda var_1, var_2: var_1 * var_2, my_list)
print(final_count)
