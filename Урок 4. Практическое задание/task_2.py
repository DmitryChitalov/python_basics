"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

Реализуйте вариант без и с генераторным выражением
"""

# С генераторным выражением
my_list = [int(el) for el in input("Введите числа через пробел: ").split()]
result_list = [my_list[i + 1] for i in range(len(my_list) - 1) if my_list[i + 1] > my_list[i]]
print(result_list)

# Без генераторного выражения
input_text = input("Введите числа через пробел: ").split()
new_result_list = []
for el in input_text:
    int(el)
for i in range(len(input_text) - 1):
    if input_text[i + 1] > input_text[i]: new_result_list.append(input_text[i + 1])
print(result_list)
