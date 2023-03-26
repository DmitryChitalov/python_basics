"""
4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо
выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень!
ВНИМАНИЕ: использование встроенной функции = задание не принято
Постараться придумать свой алгоритм без **
"""

# Вариант 1
'''
def my_func(value1, value2):
    return value1 ** value2


first_number = int(input("Введите число для возведения в степень: "))
second_number = int(input("Введите степень: "))
print(my_func(first_number, second_number))
'''


# Вариант 2

def my_func(value1, value2):
    first_number = value1
    if value2 > 0:
        for elem in range(1, value2):
            first_number *= value1
    else:
        for elem in range(1, value2, -1):
            first_number /= value1
    return first_number


user_number1 = (input("Введите число для возведения в степень: "))
user_number2 = int(input("Введите степень: "))
print(my_func(user_number1, user_number2))
