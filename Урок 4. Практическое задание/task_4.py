"""
4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генераторное выржаение.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
"""
list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
unique_elements = []
for el in list:
    if el not in unique_elements:
        unique_elements.append(el)
counter_of_elements = {uniq_el: sum([uniq_el==el for el in list]) for uniq_el in unique_elements}
result = [el for el in counter_of_elements if counter_of_elements[el] == 1]
print(result)