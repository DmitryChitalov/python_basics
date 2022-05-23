"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def find_max_between_two(param1, param2):
    return param1 if param1 > param2 else param2


def my_func(param1,  param2, param3):
    return find_max_between_two(param1, param2) + find_max_between_two(param2, param3)


def my_func_with_sort(param1,  param2, param3):
    some_list: list = [param1, param2, param3]
    some_list.sort()
    return some_list[2] + some_list[1]


print(f"Результат без sort {my_func(1, 2, 3)}")
print(f"Результат c sort {my_func_with_sort(3, 2, 1)}")
