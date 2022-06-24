"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""

'''Способ с функцией sort()'''
def my_func(a, b, c):
    z = [a, b, c]
    z.sort()
    temp = z[1:3]
    temp = temp[0] + temp[1]
    return temp


print(my_func(22, 20, 11))


'''Способ без функциии sort()'''
def my_func(a, b, c):
    if a >= b >= c:
        return a + b
    elif a >= b <= c:
        return a + c
    else:
        return b + c


print(my_func(12, 10, 12))
