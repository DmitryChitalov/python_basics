"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

Реализуйте вариант без и с генераторным выражением
"""
#!/usr/bin/env python3
initial_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result_list = []

for i in range(len(initial_list) - 1):
    if initial_list[i] < initial_list[i + 1]:
        result_list.append(initial_list[i + 1])

print(result_list[1:])
result_with_lc_list = [i for i in range(initial_list) if initial_list[i] < initial_list[i + 1]]
print(result_with_lc_list)
