"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

Реализуйте вариант без и с генераторным выражением
"""

# Вариант 1 (без генератора)
list1 = [18, 1, 30, 2, 8, 10]
print(list1)
k = len(list1)
list2 = []
for i in range(0, k):
    # print(list1[i])
    if i > 0:
        if list1[i] > list1[i - 1]:
            list2.append(list1[i])
    else:
        list2.append(list1[i])
print(list2)

# Или через  list comprehension
list1 = [18, 1, 30, 2, 8, 10]
print(list1)
k = len(list1)
list2 = []
list2 = [list1[el] for el in range(1, k) if
         list1[el] > list1[el - 1]]  # сравнение текущего и предыдущего элемента списка
print(list2)

# Вариант 2 (с генератором)
print(f"Вариант 2 с генератором")
list_1 = [4, 8, 8, 2, 18, 15, 35, 100]
print(list_1)
k = len(list_1)
generator = (list_1[el] for el in range(1, k) if list_1[el] > list_1[el - 1])
for el in generator:
    print(el)


