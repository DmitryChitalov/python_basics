"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

Реализуйте вариант без и с генераторным выражением
"""

from itertools import filterfalse

MIN_THRESHOLD = 50

list_num = [130, 25, 13, 54, 88, 11, 43, 76, 99, 51, 64, 86, 111, 36]
print(f"Исходный список: {list_num}")

list_for = []
for el in list_num:
    if el > MIN_THRESHOLD:
        list_for.append(el)
print(f"С помощью for-in: {list_for}")

list_gen = [el for el in list_num if el > MIN_THRESHOLD]
print(f"С помощью генератора: {list_gen}")

list_filter_false = list(filterfalse(lambda i: i <= MIN_THRESHOLD, list_num))
print(f"С помощью filterfalse: {list_filter_false}")
