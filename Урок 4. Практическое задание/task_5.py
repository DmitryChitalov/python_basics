"""
5. Реализовать формирование списка, используя функцию range()
и возможности генераторного выражения.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать лямбда-функцию и функцию reduce().
"""
from functools import reduce


def multiplicate(mult_res, next_val):
    """Функция умножения"""
    return mult_res * next_val


lst = [i for i in range(100, 1001) if i % 2 == 0]
mult_total = reduce(multiplicate, lst)

print(lst)
print(mult_total)
