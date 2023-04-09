"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

Реализуйте вариант без и с генераторным выражением
"""
my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 44]

print(f'Исходный список: {my_list}')

# вариант с циклом
my_list_r = []
for el in range(1, len(my_list)):
    if my_list[el] > my_list[el - 1]:
        my_list_r.append(my_list[el])
print(f'Элементы исходного списка,значения которых больше предыдущего: {my_list_r}')

# вариант с использованием LC
my_list_r2 = [my_list[el] for el in range(1, len(my_list)) if my_list[el] > my_list[el - 1]]
print(f'Элементы исходного списка,значения которых больше предыдущего: {my_list_r2}')
