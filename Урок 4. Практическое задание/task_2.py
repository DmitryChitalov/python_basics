"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

Реализуйте вариант без и с генераторным выражением
"""


global_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

# 1 вариант

first_list = []
for el in range(1, len(global_list)):
    if global_list[el] > global_list[el-1]:
        first_list.append(global_list[el])
print(first_list)

# 2 вариант

second_list = [global_list[el] for el in range(1, len(global_list)) if global_list[el] > global_list[el-1]]
print(second_list)

