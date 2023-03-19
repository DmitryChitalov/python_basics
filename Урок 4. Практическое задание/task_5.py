"""
5. Реализовать формирование списка, используя функцию range()
и возможности генераторного выражения.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать лямбда-функцию и функцию reduce().
"""
from functools import reduce
def mul_list(el_1, el_2):
    return el_1 * el_2

uniq_list = [el for el in range(100,1001,2)]
print(f"List\n{uniq_list}\nMultiplication of numbers\n{reduce(mul_list, uniq_list)}")