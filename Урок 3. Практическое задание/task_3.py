"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""
def my_func(*arg):
    arg_1 = int(input("Введите первый аргумент: "))
    arg_2 = int(input("Введите второй аргумент: "))
    arg_3 = int(input("Введите третий аргумент: "))

    if arg_1 >= arg_2 > arg_3:
        return arg_1 + arg_2
    elif arg_3 >= arg_2 > arg_1:
        return arg_3 + arg_2
    elif arg_1 >= arg_3 > arg_2:
        return arg_1 + arg_3

print(my_func())
