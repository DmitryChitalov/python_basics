"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


"""Функция суммы 2-х максимальных значений из 3-х с сортировкой """


def with_sort(arg1, arg2, arg3):
    sort_list = [arg1, arg2, arg3]
    sort_list.sort(reverse=True)
    res_sum = sort_list[0] + sort_list[1]
    return res_sum


"""Функция суммы 2-х максимальных значений из 3-х без сортировкой """


def without_sort(arg1, arg2, arg3):
    sort_list = [arg1, arg2, arg3]
    sort_list.remove(min(sort_list))
    res_sum = sum(sort_list)
    return res_sum


try:
    num_1 = float(input("Введите первое число: "))
    num_2 = float(input("Введите второе число: "))
    num_3 = float(input("Введите третье число: "))
    print(f"Результат сумма двух наибольших значений с сортировкой = {with_sort(num_1, num_2, num_3)}")
    print(f"Результат сумма двух наибольших значений без сортировки = {without_sort(num_1, num_2, num_3)}")
except ValueError:  # проверка корректности ввода данных
    print("Необходимо вводить цифры")
