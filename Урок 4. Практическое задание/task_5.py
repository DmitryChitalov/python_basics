"""
5. Реализовать формирование списка, используя функцию range()
и возможности генераторного выражения.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать лямбда-функцию и функцию reduce().
"""
from functools import reduce

list1 = [i for i in range(100, 1001, 2)]
print(list1)
list2 = reduce(lambda x, y: x * y, list1)
print(list2)