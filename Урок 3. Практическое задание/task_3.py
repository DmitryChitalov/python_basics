"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""

# Первое решение
def my_func(arg_1, arg_2, arg_3):
    b = [arg_1, arg_2, arg_3]
    b.sort(reverse=True)
    print(b[0] + b[1])


my_func(21, 3, 9)

# Второе решение
def my_func_1(arg_1, arg_2, arg_3):
    b = [arg_1, arg_2, arg_3]
    b.remove(min(b))
    return print(sum(b))


my_func_1(1, 7, 5)







