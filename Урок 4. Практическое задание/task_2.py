"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

Реализуйте вариант без и с генераторным выражением
"""
my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

def new_list_func(list_from_new_list):
    new_list = []
    for i in range(len(list_from_new_list) - 1):
        if list_from_new_list[i] < list_from_new_list[i + 1]:
            new_list.append(list_from_new_list[i + 1])
    return new_list
new_list_first = new_list_func(my_list)
print(new_list_first) 

new_list_second = [my_list[i + 1] for i in range(len(my_list) - 1) if my_list[i + 1] > my_list[i]]
print(new_list_second)