"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

Реализуйте вариант без и с генераторным выражением
"""


def find_befor_min(input_list):
    new_list = []
    for x in range(len(input_list) - 1):
        if input_list[x] < input_list[x + 1]:
            new_list.append(input_list[x + 1])
    return new_list


current_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
generated_list = [round(el*0.23) for el in current_list]

print(find_befor_min(current_list))
print(find_befor_min(generated_list))

