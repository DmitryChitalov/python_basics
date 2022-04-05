"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def my_func(my_arg1, my_arg2, my_arg3):
    my_list = [my_arg1, my_arg2, my_arg3]
    my_list.sort(reverse=True)
    return my_list[0] + my_list[1]


print(f"С функцией sort {my_func(5, 2, 3)}")


def my_func1(my_arg1, my_arg2, my_arg3):
    if my_arg1 >= my_arg2 and my_arg3 >= my_arg2:
        return my_arg1 + my_arg3
    elif my_arg1 >= my_arg2 and my_arg2 >= my_arg3:
        return my_arg1 + my_arg2
    else:
        my_arg2 + my_arg3


print(f"Без функции sort {my_func(5, 2, 3)}")
