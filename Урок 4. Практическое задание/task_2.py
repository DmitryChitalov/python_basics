"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

Реализуйте вариант без и с генераторным выражением
"""
from random import randint


def values_greater_previous(original_list):
    rez_list = []
    for i in range(len(original_list) - 1):
        if original_list[i + 1] > original_list[i]:
            rez_list.append(original_list[i + 1])
    return rez_list


my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(my_list)
print(values_greater_previous(my_list))

my_list_1 = [randint(0, 100) for i in range(20)]
print(my_list_1)
print(values_greater_previous(my_list_1))
