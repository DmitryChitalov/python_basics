"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

Реализуйте вариант без и с генераторным выражением
"""
list_in = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

list_1 = []
for i in range(1, len(list_in)):
    if list_in[i] > list_in[i - 1]:
        list_1.append(list_in[i])

list_2 = [list_in[i] for i in range(1, len(list_in)) if list_in[i] > list_in[i - 1]]

print(list_1)
print(list_2)
