"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""
arg1 = int(input("1 аргумент "))
arg2 = int(input("2 аргумент "))
arg3 = int(input("3 аргумент "))
def my_func(arg1, arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg2 >= arg1 and arg3 >= arg1:
        return arg2 + arg3
    elif arg1 >= arg2 and arg3 >= arg2:
        return arg1 + arg3
print(f'Результат без функции sort() - {my_func(arg1, arg2, arg3)}')

def my_sort(ar1, ar2, ar3):
    my_list = [ar1, ar2, ar3]
    my_list.sort()
    res = int(my_list[1]) + int(my_list[2])
    return print(f'Результат используя функцию sort()- {res}')
my_sort(input("1 аргумент "), input("2 аргумент "), input("3 аргумент "))
