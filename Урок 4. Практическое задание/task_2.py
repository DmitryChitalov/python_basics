"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

Реализуйте вариант без и с генераторным выражением
"""

from random import randint


def lst_compare(lst):
    return [lst[idx] for idx in range(1, len(lst))
            if lst[idx] > lst[idx - 1]]


def lst_random(lst_len):
    return [randint(0, 1000) for x in range(lst_len)]


def lst_compare_simple(lst):
    result = []
    for i in range(1, len(lst)):
        if lst[i] > lst[i - 1]:
            result.append(lst[i])
    return result


rand_lst = lst_random(12)

print(f"Без генератора, исходный массив: {rand_lst}")
print(f"Без генератора, результат: {lst_compare_simple(rand_lst)}")

print(f"С генератором, исходный массив: {rand_lst}")
print(f"С генератором, результат: {lst_compare(rand_lst)}")
