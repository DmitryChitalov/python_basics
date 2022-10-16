'''
Реализовать функцию my_func(), которая принимает три позиционных
аргумента и возвращает сумму наибольших двух аргументов.
'''


def my_func(*args):
    args1 = int(input("args1: "))
    args2 = int(input("args2: "))
    args3 = int(input("args3: "))

    if args1 >= args2 > args3:
        return args1 + args2
    elif args3 >= args2 > args1:
        return args3 + args2
    elif args1 >= args3 > args1:
        return args1 + args3
    else:
        exit(-1)


print(my_func())
