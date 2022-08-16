"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

Реализуйте вариант без и с генераторным выражением
"""
# Первый вариант
lst = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55, 65]
new_lst = [lst[i] for i in range(1, len(lst)) if lst[i] > lst[i - 1]]
print(new_lst)

# Второй вариант
new_lst = []
for i in range(1, len(lst)):
    if lst[i] > lst[i - 1]:
        new_lst.append(lst[i])
print(new_lst)


# Выриант с генераторным выражением. Но непонятен смысл
generator = (lst[i] for i in range(1, len(lst)) if lst[i] > lst[i - 1])
new_lst = []
n = 0
for i in generator:
    new_lst.append(i)
print(new_lst)