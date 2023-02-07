"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

Реализуйте вариант без и с генераторным выражением
"""

orig_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

# without LC
result_list = []
for i in range(1, len(orig_list)):
    if orig_list[i] > orig_list[i -1]:
        result_list.append(orig_list[i])
print(result_list)

# with LC
result_lc_list = [orig_list[i] for i in range(1, len(orig_list)) if orig_list[i] > orig_list[i - 1]]
print(result_lc_list)