"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

Реализуйте вариант без и с генераторным выражением
"""

list_number = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [list_number[i] for i in range(1, len(list_number)) if list_number[i-1] < list_number[i]]
print("Результат: " + str(new_list))

second_list = []
my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
for i in range(1, len(my_list)):
    if my_list[i] > my_list[i-1]:
        second_list.append(my_list[i])
print("Результат: " + str(second_list))


"""
generator = (el for el in range(1, len(my_list)))
for el in generator:
    if my_list[el] > my_list[el-1]:
        print(my_list[el])"""