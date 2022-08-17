"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

Реализуйте вариант без и с генераторным выражением
"""
lst = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_lst = []
for i in range(len(lst)):
    if i == 0:
        continue
    if lst[i - 1] < lst[i]:
        new_lst.append(lst[i])
print(new_lst)

in_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
res_list = [number for i, number in enumerate(in_list) if i > 0 and in_list[i] > in_list[i - 1]]
print(res_list)
