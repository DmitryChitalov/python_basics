"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""
def my_func(var_1, var_2, var_3):
    arg_list = [var_1, var_2, var_3]
    arg_list.sort(reverse=True)
    return arg_list[0] + arg_list[1]
def my_func2(var_1, var_2, var_3):
    x = [var_1, var_2, var_3]
    args_list = [x.pop(x.index(max(x))), max(x)]
    return args_list[0] + args_list[1]
print(my_func(220, 180, 200))
print(my_func2(302, 303, 301))
