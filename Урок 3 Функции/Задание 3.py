"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму
наибольших двух аргументов.
"""

arg = input('Enter 3 arguments for function: ').split()


def my_func(a_1, a_2, a_3):
    """
    Функция принимает 3 аргумента: a_1, a_2, a_3, и выводит сумму наибольших двух
    (int, int, int) -> int

    #>>> print(my_func(arg[0], arg[1], arg[2]))
    Enter 3 arguments for function: 1 5 7
    12
    """

    lst = [a_1, a_2, a_3]
    for el in range(len(lst)):
        lst[el] = int(lst[el])
    lst.remove(min(lst))
    return sum(lst)


print(my_func(arg[0], arg[1], arg[2]))
