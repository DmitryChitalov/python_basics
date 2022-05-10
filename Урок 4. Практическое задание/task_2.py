"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Пример исходного списка: [2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

Реализуйте вариант без и с генераторным выражением
"""


##Enumerate
g_list = [2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_g_list = [el for num, el in enumerate(g_list) if g_list[num -1] < g_list[num]]
print(f'Initial List: {g_list}')
print(f'Generated List: {new_g_list}')

##Range
list_number = [2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [list_number[i] for i in range(len(list_number)) if list_number[i-1] < list_number[i]]
print('Initial List: ' + str(list_number))
print('W/Generate List: ' + str(new_list))
