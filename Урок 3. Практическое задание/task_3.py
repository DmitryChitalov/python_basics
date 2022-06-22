"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def sum_max(param_1, param_2, param_3):
    """
    Возвращает сумму двух наибольших аргументов - используется сортировка
    :param param_1: первый аргумент функции - число
    :param param_2: второй аргумент фукнции - число
    :param param_3: третий аргумент функции - число
    :return: сумма двух максимальных параметров
    """
    input_list = [param_1, param_2, param_3]
    input_list.sort(reverse=True)
    input_list = input_list[:2]
    return sum(input_list)


def sum_two_max(param_1, param_2, param_3):
    """
    Возвращает сумму двух наибольших аргументов - сортировка не используется
    :param param_1: первый аргумент функции - число
    :param param_2: второй аргумент фукнции - число
    :param param_3: третий аргумент функции - число
    :return: сумма двух максимальных параметров
    """
    out_list = [param_1, param_2, param_3]
    min_el = min(out_list)
    out_list.remove(min_el)
    return sum(out_list)


print(sum_max(1, 1, 1))
print(sum_two_max(1, 1, 1))







