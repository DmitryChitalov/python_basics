# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти чётные числа от 100 до 1000 (включая границы).
# Нужно получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce

my_list = [el for el in range (100, 1001, 2)]
print(my_list)
res = reduce(lambda el1, el2: el1*el2, my_list)
print(res)
