"""
5. Реализовать формирование списка, используя функцию range()
и возможности генераторного выражения.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать лямбда-функцию и функцию reduce().
"""
from functools import reduce
original_list = [num for num in range(100, 1001, 2)]
print(original_list)
result = reduce(lambda size, size2: size * size2, original_list)
print(f"Результат: {result}")
