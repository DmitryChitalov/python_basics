"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""
# 1) используя функцию sort()
def get_max(*args):
    print(sum(sorted(list(args), reverse=True)[:2]))

get_max(4, 5, 6)

# 2) без функции sort()
def my_func(arg1, arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 > arg2 and arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3


try:
    first_num = int(input("Введите первый аргумент (целое число):  "))
    second_num = int(input("Введите второй аргумент (целое число):  "))
    third_num = int(input("Введите третий аргумент (целое число):  "))
    print (my_func(first_num, second_num, third_num))
except ValueError:
    print("Вводите только целые числа")
