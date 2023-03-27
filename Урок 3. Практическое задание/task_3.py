"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""

# Вариант 1 - с функцией sort


def my_func1(var_1, var_2, var_3):
    my_list = [var_1, var_2, var_3]
    my_list.sort(reverse=True)
    return my_list[0] + my_list[1]


print(my_func1(10, 60, -1))

# Вариант 2 - без функции sort


def my_func2(var_1, var_2, var_3):
    my_list = [var_1, var_2, var_3]

    def sort_bubble(my_list1):  # сортировка входящего массива методом пузырька
        list_len = len(my_list1)
        iterator_1 = 0
        while iterator_1 < list_len-1:
            iterator_2 = 0
            while iterator_2 < list_len - 1 - iterator_1:
                if my_list1[iterator_2] > my_list1[iterator_2 + 1]:
                    my_list1[iterator_2], my_list1[iterator_2 + 1] = my_list1[iterator_2 + 1], my_list1[iterator_2]
                iterator_2 += 1
            iterator_1 += 1
        return my_list1
    res_list = sort_bubble(my_list)
    return res_list[len(res_list)-1] + res_list[len(res_list)-2]


print(my_func2(10, 60, -1))
