"""
5. Реализовать формирование списка, используя функцию range()
и возможности генераторного выражения.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать лямбда-функцию и функцию reduce().
"""
from functools import reduce

# Вариант 1
a = (x for x in range(100, 1001, 2))
lst = []
for x in a:
    lst.append(x)
print(lst)
print(reduce(lambda x, y: x * y, lst))

# Вариант 2
new_lst = [el for el in range(100, 1001, 2)]
print(new_lst)
print(reduce(lambda x, y: x * y, new_lst))