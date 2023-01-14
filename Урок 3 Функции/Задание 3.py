"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму
наибольших двух аргументов.
"""

arg = input('Enter 3 arguments for function: ').split()


def my_func(a, b, c):
    lst = [a, b, c]
    for _ in range(len(lst)):
        lst[_] = int(lst[_])
    lst.remove(min(lst))
    return sum(lst)


print(my_func(arg[0], arg[1], arg[2]))

"""
Enter 3 arguments for function: 1 5 7
12
"""
