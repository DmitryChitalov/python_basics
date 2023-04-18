"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

Реализуйте вариант без и с генераторным выражением
"""
from functools import reduce
def generate_new_list(origin_list):
    new_list = []
    for i in range(0,len(origin_list)-1):
        if origin_list[i+1] > origin_list[i]:
            new_list.append(origin_list[i+1])
    return new_list


origin_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(generate_new_list(origin_list))