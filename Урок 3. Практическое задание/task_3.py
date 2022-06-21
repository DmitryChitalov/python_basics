"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def my_func(arg1, arg2, arg3):
    srt_items = [arg1, arg2, arg3]
    srt_items.remove(min(srt_items))

    return sum(srt_items)


print(my_func(77, 1, 88))


def max_func(arg1, arg2, arg3):
    list_arg = [arg1, arg2, arg3]
    print(sum(sorted(list_arg, reverse=True)[:2]))


max_func(125, 1, 10)
