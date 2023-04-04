"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

Реализуйте вариант без и с генераторным выражением
"""

def_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(f"Исходный список: {def_list}")

# с циклом while
new_list_while = []
i = 1
while i < len(def_list):
    if def_list[i] > def_list[i - 1]:
        new_list_while.append(def_list[i])
    i += 1
print(f"Результат с циклом while: {new_list_while}")

# с циклом for
new_list_for = []
num = def_list[0]
for el in def_list:
    if el > num:
        new_list_for.append(el)
    num = el
print(f"Результат с циклом for: {new_list_for}")

# с генератором
new_list_gen = [def_list[el] for el in range(1, len(def_list)) if def_list[el] > def_list[el - 1]]
print(f"Результат с генератором списка: {new_list_gen}")
