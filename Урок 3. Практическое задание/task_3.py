"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""
# def my_func(arg1, arg2, arg3):
#     if arg1 >= arg3 and arg2 >= arg3:
#         return arg1 + arg2
#     elif arg1 > arg2 and arg1 < arg3:
#         return arg1 + arg3
#     else:
#         return arg2 + arg3
# print(my_func(int(input('Введите число 1: ')), int(input('Введите число 2: ')), int(input('Введите число 3: '))))

def my_func(arg1, arg2, arg3):
    a = [arg1,arg2,arg3]
    a.sort(reverse = True)
    return a[0]+a[1]
print(my_func(int(input('Введите число 1: ')), int(input('Введите число 2: ')), int(input('Введите число 3: '))))