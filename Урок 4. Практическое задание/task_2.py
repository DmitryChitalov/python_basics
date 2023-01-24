"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

Реализуйте вариант без и с генераторным выражением
"""

source_list = [1, 3, 4, 1, 1, 2, 10]

# Вариант без генератора
result_list_1 = []
for i in range(1, len(source_list)):
    if source_list[i] > source_list[i-1]:
        result_list_1.append(source_list[i])
    else:
        continue
    i = i + 1

# Вариант с генератором
result_list_2 = [source_list[el] for el in range(1, len(source_list)) if source_list[el] > source_list[el-1]]

print(f'Исходный список: {source_list}')
print(f'Результат 1: {result_list_1}')
print(f'Результат 2: {result_list_2}')


