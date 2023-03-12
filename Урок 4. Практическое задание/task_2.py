"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

Реализуйте вариант без и с генераторным выражением
"""

def calc_without_ls(list):
    result = []
    for i in range(1, len(list)):
        if (list[i] > list[i - 1]):
            result.append(list[i])
    return result

def calc_with_ls(list):
    return [list[i] for i in range(1, len(list)) if list[i] > list[i - 1]]

source_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print("Вариант 1:", calc_without_ls(source_list))
print("Вариант 2:", calc_with_ls(source_list))