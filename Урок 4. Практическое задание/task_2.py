"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

Реализуйте вариант без и с генераторным выражением
"""
original_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
######## без генератора

new_list = []
i = 1
while i < len(original_list):
    if original_list[i] > original_list[i-1]:
        new_list.append(original_list[i])
    i += 1
print(new_list)
######### с генераторным выражением

new_list_generated = [ original_list[i] for i in range(1, len(original_list)) if original_list[i] > original_list[i-1]]
print(new_list_generated)