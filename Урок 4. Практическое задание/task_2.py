"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

Реализуйте вариант без и с генераторным выражением
"""
INITIAL_LIST = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
results_list = []
for i in range(1, len(INITIAL_LIST)):
    if INITIAL_LIST[i] > INITIAL_LIST[i - 1]:
        results_list.append(INITIAL_LIST[i])
print(f'Результат без генераторного выражения: {results_list}')
gen_results_list = [INITIAL_LIST[i] for i in range(1, len(INITIAL_LIST)) \
                    if INITIAL_LIST[i] > INITIAL_LIST[i - 1]]
print(f'Результат c генераторным выражением: {gen_results_list}')
