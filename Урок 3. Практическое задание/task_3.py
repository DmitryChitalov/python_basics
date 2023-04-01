"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def my_func(a,b,c):
    if b > a and c > a:
        return print(b + c)
    elif a > b and c > b:
        return print(a + c)
    elif a > c and b > c:
        return print(a + b)
    else:
        print("что то не так")

my_func(1,5,3)

def my_func_s(q,w,e):
    g = [q,w,e]
    g.sort()
    return print(g[1]+g[2])
my_func_s(1,5,3)