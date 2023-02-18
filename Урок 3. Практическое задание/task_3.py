"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def max_sum_two(n1, n2, n3):
    """
    returns the sum of the largest two arguments
    :param int|float n1: number
    :param int|float n2: number
    :param int|float n3: number
    :return: sum
    """
    if False in [isinstance(n1, (int, float)), isinstance(n2, (int, float)), isinstance(n3, (int, float))]:
        return None
    lst = [n1, n2, n3]
    lst.sort()
    return lst[-1] + lst[-2]


def max_sum_two2(n1, n2, n3):
    """
    returns the sum of the largest two arguments
    :param int|float n1: number
    :param int|float n2: number
    :param int|float n3: number
    :return: sum
    """
    if False in [isinstance(n1, (int, float)), isinstance(n2, (int, float)), isinstance(n3, (int, float))]:
        return None
    lst = [n1, n2, n3]
    a = lst.pop(lst.index(max(lst)))
    b = lst.pop(lst.index(max(lst)))
    return a + b


print(max_sum_two(6, 8, 5))
print(max_sum_two2(1, 6, 2))
