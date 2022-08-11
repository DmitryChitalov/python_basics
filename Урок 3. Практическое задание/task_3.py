"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def my_func(arg1, arg2, arg3, with_sort=False):
    if with_sort:
        my_list = [arg1, arg2, arg3]
        my_list.sort()
        max_sum = my_list[1] + my_list[2]
    else:
        if arg1 > arg2:
            if arg2 > arg3:
                max_sum = arg1 + arg2
            else:
                max_sum = arg1 + arg3
        else:
            max_sum = arg2 + arg3
    return max_sum


a = int(input("Первое число:"))
b = int(input("Второе число:"))
c = int(input("Третье число:"))

print("Результат через функцию sort(): ", my_func(a, b, c, True))
print("Результат без функции sort(): ", my_func(a, b, c))
