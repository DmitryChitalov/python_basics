"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

Реализуйте вариант без и с генераторным выражением
"""


def my_list_1(func_list):
    new_list = []
    for i in range(1, len(func_list)):
        if func_list[i] > func_list[i-1]:
            new_list.append(func_list[i])
    print(new_list)


def my_list(func_list):
    new_list = [func_list[i] for i in range(1, len(func_list))
                if func_list[i] > func_list[i-1]]
    return new_list

print(my_list(input('Введите последовательность чисел через пробел: ').split()))
print(my_list_1(input('Введите последовательность чисел через пробел: ').split()))