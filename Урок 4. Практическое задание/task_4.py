"""
4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генераторное выржаение.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
"""

import list_extension

input_str = input("Please, input list of numbers separated by space: ")
input_list = input_str.split(" ")
number_list = list_extension.get__int_numbers_from_list(input_list)

unique_list = [el for el in number_list if number_list.count(el) == 1]
print(unique_list)