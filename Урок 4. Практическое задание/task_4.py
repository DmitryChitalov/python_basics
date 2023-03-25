"""
4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генераторное выржаение.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]

"генераторное выржаение" здесь List comprehension 
"""
#!/usr/bin/env python3
initial_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
loopy_result_list = []
lc_result_list = []
for i in initial_list:
    if initial_list.count(i) < 2:
        loopy_result_list.append(i)
    else:
        pass

lc_result_list = [i for i in initial_list if initial_list.count(i) < 2 ]
print(loopy_result_list)
print(lc_result_list)
