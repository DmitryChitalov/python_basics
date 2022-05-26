"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""
def my_func(a, b, c):
    if a>b and c>b:
        return a+c
    elif b>a and c>a:
        return b+c
    elif a>c and b>c:
        return a+b

print(my_func(1,22,3))


def func(a,b,c):
    lis = []
    lis.append(a)
    lis.append(b)
    lis.append(c)
    lis.sort()
    return lis[-1] + lis[1]


print(func(4444,2,1))




