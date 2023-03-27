"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

Реализуйте вариант без и с генераторным выражением
"""

num_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

# Вариант с циклом while
res_list = []
i = 1
while i < len(num_list):
    if num_list[i] > num_list[i - 1]:
        res_list.append(num_list[i])
    i += 1
print(f"Новый список: {res_list}")

# Вариант с циклом for
res_list = []
dif = num_list[0]
for el in num_list:
    if el > dif:
        res_list.append(el)
    dif = el
print(f"Новый список: {res_list}")

# Вариант с генератором списка (list comprehensions)
res_list = [num_list[index] for index in range(1, len(num_list)) if num_list[index] > num_list[index - 1]]
print(f"Новый список: {res_list}")
