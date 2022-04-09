"""
4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо
выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень!
ВНИМАНИЕ: использование встроенной функции = задание не принято
Постараться придумать свой алгоритм без **
"""

import string_extension

def negative_power(num_1, num_2):
    iterator = 0
    result = num_1 / num_2
    while iterator < abs(num_2) - 1:
        result = result / num_2
        iterator += 1
    return result

input_num_1 = input("Please, input first positive number: ")
input_num_2 = input("Please, input second negative number: ")

if string_extension.is_float(input_num_1) and string_extension.is_int(input_num_2):
    num_1 = float(input_num_1)
    num_2 = int(input_num_2)

    if num_1 >= 0 and num_2 < 0:
        print(negative_power(num_1, num_2))
    else:
        if num_1 < 0:
            print(f"First number ({num_1}) is not a positive number")
        if num_2 >= 0:
            print(f"Second number ({num_2}) is not a negative number")
else:
    print(f"Error: one of your input values is not a number")