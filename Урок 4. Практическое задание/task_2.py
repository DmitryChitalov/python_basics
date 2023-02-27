"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

Реализуйте вариант без и с генераторным выражением
"""

#Вариант решения задачи без генераторного выражения:
def find_larger_nogen(lst):
    result = []
    for i in range(1, len(lst)):
        if lst[i] > lst[i-1]:
            result.append(lst[i])
    return result

# Вариант решения задачи с генераторным выражением:
def find_larger_gen(lst):
    return [lst[i] for i in range(1, len(lst)) if lst[i] > lst[i-1]]


lst = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

larger_nogen = find_larger_nogen(lst)
larger_gen = find_larger_gen(lst)
print(larger_nogen, larger_gen)