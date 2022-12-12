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
        return (f"Функция без sort: {sum_1}")
    elif sum_2 > sum_3:
        return (f"Функция без sort: {sum_2}")
    return (f"Функция без sort: {sum_3}")
print(my_func(4, 3, -2))


def my_func_1(*nums):
    s_num = sorted(nums)
    s_sum = s_num[-1] + s_num[-2]
    return (f"Функция с sort: {s_sum}")

print(my_func_1(4, 3, -2))
