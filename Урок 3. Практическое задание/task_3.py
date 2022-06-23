"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def my_func1(x, y, z):
    my_list = [x, y, z]
    my_list.sort(reverse=True)
    return print(my_list[0] + my_list[1])


def my_func2(x, y, z):
    if x + y > y + z:
        return print(x + y)
    return print(y + z)


my_func1(x=1, y=2, z=3)
my_func2(x=1, y=2, z=3)
