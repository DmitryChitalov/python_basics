"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""

def my_func(arg_1, arg_2, arg_3):
    sum_1 = arg_1 + arg_2
    sum_2 = arg_2 + arg_3
    sum_3 = arg_1 + arg_3
    if sum_1 > sum_2 and sum_1 > sum_3:
        return sum_1
    elif sum_2 > sum_3:
        return sum_2
    return sum_3
print(f"Функция без sort: {my_func(1, 1, 1)}")


def my_func_1(*nums):
    s_num = sorted(nums)
    s_sum = s_num[-1] + s_num[-2]
    return s_sum
print(f"Функция с sort: {my_func_1(3, 0, -1)}")
