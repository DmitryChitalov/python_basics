"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

Реализуйте вариант без и с генераторным выражением
"""


my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

# 1 без LC
next_list_1 = []
for x in range(1, len(my_list)):
    if my_list[x] > my_list[x - 1]:
        next_list_1.append(my_list[x])

print(next_list_1)

# 2 с LC
next_list_2 = [my_list[x] for x in range(1, len(my_list)) if my_list[x] > my_list[x - 1]]

print(next_list_2)

# 3 c LC без списка
print([my_list[x] for x in range(1, len(my_list)) if my_list[x] > my_list[x - 1]])
