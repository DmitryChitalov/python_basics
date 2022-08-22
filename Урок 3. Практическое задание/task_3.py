"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def my_func(num_1, num_2, num_3):
    my_list = [num_1, num_2, num_3]
    my_list.remove(min(my_list))
    return print(f"без функции sort: {my_list[0] + my_list[1]}")


def my_func_2(num_1, num_2, num_3):
    my_list = [num_1, num_2, num_3]
    my_list.sort(reverse=True)
    return print(f"используя функцию sort: {my_list[0] + my_list[1]}")


var_1 = int(input("Введите первое число: "))
var_2 = int(input("Введите второе число: "))
var_3 = int(input("Введите третье число: "))
my_func(var_1, var_2, var_3)
my_func_2(var_1, var_2, var_3)
