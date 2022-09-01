"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

Реализуйте вариант без и с генераторным выражением
"""
#вариант 1
original_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result_list_1 = []
for element in range(1, len(original_list)):
    if original_list[element] > original_list[element-1]:
        result_list_1.append(original_list[element])
print(result_list_1)

#вариант 2
result_list_2 = [original_list[element] for element in range(
    1,len(original_list)) if original_list[element] > original_list[element - 1]]
print(result_list_2)

