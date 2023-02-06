"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

Реализуйте вариант без и с генераторным выражением
"""
primary_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
var_list_1 = []
for el in range(1, len(primary_list)):
    if primary_list[el] > primary_list[el - 1]:
        var_list_1.append(primary_list[el])
print(var_list_1)
var_list_2 = [primary_list[el] for el in range(
    1, len(primary_list)) if primary_list[el] > primary_list[el - 1]]
print(var_list_2)
