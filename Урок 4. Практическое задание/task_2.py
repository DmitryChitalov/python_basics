"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

Реализуйте вариант без и с генераторным выражением
"""

#task_2

init_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(f"Пример искодного списка: {init_list}")
final_list = []
for i in range(1, len(init_list)):
    if i > 0:
        if init_list[i] > init_list[i - 1]:
            final_list.append(init_list[i])
    else:
        final_list.append(init_list[i])
print(f"Результат: {final_list}")


# вариант с генераторном выражений

init_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(f"Пример искодного списка: {init_list}")
final_list = []
generator = (init_list[el] for el in range(1, len(init_list)) if init_list[el] > init_list[el - 1])
for el in generator:
    final_list.append(el)
print(f"Результат: {final_list}") 
