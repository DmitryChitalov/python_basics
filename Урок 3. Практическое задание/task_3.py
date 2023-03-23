"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""

def my_func_1(arg_1, arg_2, arg_3):
    """
    Функция возвращает сумму наибольших двух аргументов, используя функцию sort()
    :param arg_1: аргумент 1
    :param arg_2: аргумент 2
    :param arg_3: аргумент 3
    :return: Сумма наибольших двух аргументов
    """
    my_list = [arg_1, arg_2, arg_3]
    my_list.sort()
    return my_list[-1] + my_list[-2]

def my_func_2(arg_1, arg_2, arg_3):
    """
    Функция возвращает сумму наибольших двух аргументов, не используя функции sort()
    :param arg_1: аргумент 1
    :param arg_2: аргумент 2
    :param arg_3: аргумент 3
    :return: Сумма наибольших двух аргументов
    """
    return max(arg_1, arg_2, arg_3) + max(min(arg_1, arg_2), min(arg_1, arg_3), min(arg_2, arg_3))

try:
    arg_1 = float(input("Введите первое число: "))
    arg_2 = float(input("Введите второе число: "))
    arg_3 = float(input("Введите третье число: "))
except ValueError:
    print("Ошибочный ввод!")
else:
    print(f"Результат, используя функцию sort(): {my_func_1(arg_1,arg_2,arg_3)}")
    print(f"Результат, без функции sort(): {my_func_2(arg_1, arg_2, arg_3)}")
