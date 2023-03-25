"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

Реализуйте вариант без и с генераторным выражением
"""

example_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

user_list = []

count = 0

for i in range(len(example_list) - 1):
    i = example_list[count]
    if i < example_list[count + 1]:
        user_list.append(example_list[count + 1])
        count += 1
    else:
        count += 1

user_list_v2 = [el for el in example_list
                if example_list.index(el) < len(example_list)
                if el > example_list[example_list.index(el) - 1] and el != example_list[0]]

print(f'{user_list} \n'
      f'{user_list_v2}')
