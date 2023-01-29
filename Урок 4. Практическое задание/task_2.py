"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

Реализуйте вариант без и с генераторным выражением
"""
orig_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

# без генераторного выражения
result_without_generator = []
for el in range(1, len(orig_list)):
    if orig_list[el] > orig_list[el-1]:
        result_without_generator.append(orig_list[el])

print(f"Результат без использования генератора: {result_without_generator}")

# с генераторным выражением
result_with_generator = [orig_list[el] for el in range(1, len(orig_list)) if orig_list[el] > orig_list[el-1]]

print(f"Результат с использованием генератора: {result_with_generator}")