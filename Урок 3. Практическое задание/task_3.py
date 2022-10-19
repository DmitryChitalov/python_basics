"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def sum_max_with_sort(arg1, arg2, arg3):
    """возвращает сумму наибольших двух аргументов используя sorted"""
    sorted_args = sorted((arg1, arg2, arg3))
    result = sum(sorted_args[1:])
    return result


print("Сумму наибольших двух аргументов из (3, -1, 7) = "
      f"{sum_max_with_sort(3, -1, 7)}")
print("Сумму наибольших двух аргументов из (-2, 1, -7) = "
      f"{sum_max_with_sort(-2, 1, -7)}\n")


def sum_max_wo_sort1(arg1, arg2, arg3):
    """возвращает сумму наибольших двух аргументов с помощью сравнения"""
    if arg1 > arg2:
        return arg1 + arg3 if arg3 > arg2 else arg1 + arg2
    return arg2 + arg3 if arg1 < arg3 else arg1 + arg2


print("Сумму наибольших двух аргументов из (3, -1, 7) = "
      f"{sum_max_wo_sort1(3, -1, 7)}")
print("Сумму наибольших двух аргументов из (2, -1, 2) = "
      f"{sum_max_wo_sort1(3, -1, 2)}")
print("Сумму наибольших двух аргументов из (-2, 1, 7) = "
      f"{sum_max_wo_sort1(-2, 1, 7)}")
print("Сумму наибольших двух аргументов из (-2, 1, -7) = "
      f"{sum_max_wo_sort1(-2, 1, -7)}\n")


def sum_max_wo_sort2(arg1, arg2, arg3):
    """возвращает сумму наибольших двух аргументов используя min"""
    return arg1 + arg2 + arg3 - min(arg1, arg2, arg3)


print("Сумму наибольших двух аргументов из (3, -1, 7) = "
      f"{sum_max_wo_sort2(3, -1, 7)}")
print("Сумму наибольших двух аргументов из (2, -1, 2) = "
      f"{sum_max_wo_sort2(3, -1, 2)}")
