"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

Реализуйте вариант без и с генераторным выражением
"""


def more_previous(lst):
    """
    Elements of the original list whose values are greater than the previous element
    :param list lst: original list
    :return: new list, error
    :rtype: (list[int|float], None) | (None, str)
    """
    try:
        res = [i for i in lst if 0 != lst.index(i) and i > lst[lst.index(i) - 1]]
        return res, None
    except Exception as e:
        return None, e


new_lst, err = more_previous([300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55])
print(new_lst)
