"""
6)	Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                                        Физика:   30(л)   —   10(лаб)
                                        Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

import re

with open('subj.txt', 'r', encoding='utf-8') as subj_info:
    result = {}

    for line in subj_info:
        l_list = [i for i in line.split() if i != '—']
        subject, hours = l_list[0][:-1], [int(re.search(r'\d+', i)[0]) for i in l_list[1:]]
        result[subject] = sum(hours)

print(result)
