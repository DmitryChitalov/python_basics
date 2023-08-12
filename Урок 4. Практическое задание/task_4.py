"""
4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генераторное выражение.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
"""


def is_unique(x, arr):
    is_exist = False
    for el in arr:
        if x == el:
            if is_exist:
                return False
            is_exist = True
    return True


my_list = [int(el) for el in input("Введите список чисел: ").split()]
result_list = [el for el in my_list if is_unique(el, my_list)]
print(result_list)
