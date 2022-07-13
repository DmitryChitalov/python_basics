"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

Реализуйте вариант без и с генераторным выражением
"""

numbers = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

# c lc
result_list = [
    val for idx, val in enumerate(numbers)
    if idx > 0 and numbers[idx - 1] < val
]

print(result_list)

# без lc
result_list2 = []
for idx in range(1, len(numbers)):
    if numbers[idx] > numbers[idx - 1]:
        result_list2.append(numbers[idx])

print(result_list2)
