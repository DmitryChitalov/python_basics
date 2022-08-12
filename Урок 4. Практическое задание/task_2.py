"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

Реализуйте вариант без и с генераторным выражением
"""
my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


def non_generator(arg1):
    new_list = []
    for el in arg1:
        if arg1.index(el) != 0:
            curr_el = el
            if curr_el > prev_el:
                new_list.append(curr_el)
        prev_el = el
    return new_list


def generator(arg1):
    """
    arg1.index(el) != 0 - убираем из вывода элемент с индексом 0, поскольку его не с кем сравнивать
    arg1.__getitem__(arg1.index(el)) > arg1.__getitem__(arg1.index(el) - 1) - берем значение элемента из списка
    по индексу и сравниваем с предыдущим arg1.index(el) - 1
    """
    new_list = [el for el in arg1 if arg1.__getitem__(arg1.index(el)) > arg1.__getitem__(arg1.index(el) - 1) and
                arg1.index(el) != 0]
    return new_list


print(f"Исходный список: {my_list}")
print(f"Новый список без генератора: {non_generator(my_list)}")
print(f"Новый список  с генератором: {generator(my_list)}")
"""
Исходный список: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
Новый список без генератора: [12, 44, 4, 10, 78, 123]
Новый список  с генератором: [12, 44, 4, 10, 78, 123]

Process finished with exit code 0
"""
