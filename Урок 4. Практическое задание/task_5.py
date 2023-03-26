"""
5. Реализовать формирование списка, используя функцию range()
и возможности генераторного выражения.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать лямбда-функцию и функцию reduce().
"""
from functools import reduce

my_list = [elem for elem in range(99, 1001) if elem % 2 == 0]
my_multiplication = reduce(lambda value1, value2: value1 * value2, my_list)
print(my_multiplication)
