"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def my_func(n_1, n_2, n_3):
    my_list = [n_1, n_2, n_3]
    my_list.remove(min(my_list))
    return f"Using no sort(): {sum(my_list)}"


def my_func_sort(arg1, arg2, arg3):
    my_list = []
    for i in (arg1, arg2, arg3):
        my_list.append(i)
    my_list.sort(reverse=True)
    return_sorted = my_list[0] + my_list[1]
    return f"Using sort(): {return_sorted}"


print(my_func(12, 8, 2))
print(my_func_sort(14, 8, 2))

# def my_func_sort(arg1, arg2, arg3):
#     my_list = [arg1, arg2, arg3]
#     return sum(sorted(my_list)[1:])
#
# print(my_func_sort(3, 12, -20))
