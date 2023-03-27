"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


# Используя функцию sorted
def my_func(*args):
    result_sorted = sorted(args)
    return result_sorted[len(result_sorted) - 1] + result_sorted[len(result_sorted) - 2]


def my_func_without_sorted(*args):
    max1 = 1
    max2 = 0
    for value in args:
        if value > max1:
            max2 = max1
            max1 = value
            continue
        max2 = value
    return max1 + max2


print(my_func(9, 4, 5, 6))
print(my_func_without_sorted(9, 4, 5, 6))

