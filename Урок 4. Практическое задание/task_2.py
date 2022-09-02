"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

Реализуйте вариант без и с генераторным выражением
"""

# Варант без list comprehention.
u_quit = 0
while u_quit != "**":
    new_list = []
    u_num_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
    print(f"Наш список........: {u_num_list}")
    any_n = u_num_list[0]
    for pos in u_num_list:
        if pos > any_n:
            new_list.append(pos)
            any_n = pos
        else:
            any_n = pos
# Вариант с list comrehention.
    new_list_lc = [u_num_list[pos] for pos in range(1, len(u_num_list))
                   if u_num_list[pos] > u_num_list[pos - 1]]

    print(f"Итоговый список no: {new_list}")
    print(f"Итоговый список lc: {new_list_lc}")

    u_quit = input("Continue - any, Quit - **: ")

''' В 25 строке была такая идея:
    new_list_lc = [el if el > any_n else ''any_n = el'' for el in u_num_list]
    Но заменить any_n на el так и не получилось.
    Ваше решение позволяет брать предыдущий элемент списка, мое нет ://
'''