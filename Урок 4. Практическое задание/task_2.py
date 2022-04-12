"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

Реализуйте вариант без и с генераторным выражением
"""

import list_extension

def get_increment_list(number_list):
    increment_list = []
    i = 0
    while i < len(number_list) - 1:
        if number_list[i] < number_list[i + 1]:
            increment_list.append(number_list[i + 1])
        i += 1
    
    gen_increment_list = [el for i, el in enumerate(number_list) if i > 0 and el > number_list[i - 1]]

    return increment_list, gen_increment_list

input_str = input("Please, input list of numbers separated by space: ")
input_list = input_str.split(" ")
number_list = list_extension.get__int_numbers_from_list(input_list)

increment_list, gen_increment_list = get_increment_list(number_list)

print(f"{increment_list}\n")
print(gen_increment_list)