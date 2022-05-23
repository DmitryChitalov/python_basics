"""
4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо
выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень!
ВНИМАНИЕ: использование встроенной функции = задание не принято
Постараться придумать свой алгоритм без **
"""


def calculate_power_version1(x, y):
    if x < 0 or y > 0:
        raise ValueError("Неуместные аргументы. 'X' должен быть больше '0', Y - меньше '0'")
    return x ** y


def calculate_power_version2(x, y):
    if x < 0 or y > 0:
        raise ValueError("Неуместные аргументы. 'X' должен быть больше '0', Y - меньше '0'")
    result = 1
    for i in range(abs(y)):
        result /= x
    return result


number = float(input("Введите число (>0): "))
power = int(input("Введите степень (<0, int): "))

print(f"Результат V1: {calculate_power_version1(number, power)}")
print(f"Результат V2: {calculate_power_version2(number, power)}")
