"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

Реализуйте вариант без и с генераторным выражением
"""

list_number = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list_1 = []
for el in range(1, len(list_number)):
    if list_number[el] > list_number[el - 1]:
        new_list_1.append(list_number[el])

print(new_list_1)
# Вариант 2
new_list_2 = [list_number[el] for el in range(1, len(list_number)) if list_number[el] > list_number[el - 1]]

print(new_list_2)

