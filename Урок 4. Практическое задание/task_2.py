"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

Реализуйте вариант без и с генераторным выражением
"""
primary_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result_list_1 = []
for i in range(1, len(primary_list)):
    if primary_list[i] > primary_list[i - 1]:
        result_list_1.append(primary_list[i])
print(result_list_1)
result_list_2 = [primary_list[i] for i in range(1, len(primary_list)) if primary_list[i] > primary_list[i - 1]]
print(result_list_2)
