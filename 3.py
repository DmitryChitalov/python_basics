"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


# №1
def my_func(*args) -> int:
    return sum(sorted(list(args))[2:0:-1])


print(my_func(1, 2, 3))
print(my_func(0, 1, 1))
print(my_func(0, 1, 2))


# №2
def my_func(*args) -> int:
    lst = list(args)
    minimal = min(lst)

    return sum([i for i in lst if i != minimal])


print(my_func(1, 2, 3))
print(my_func(0, 1, 1))
print(my_func(0, 1, 2))
