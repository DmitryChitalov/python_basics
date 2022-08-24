"""
6)	Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный
предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                                        Физика:   30(л)   —   10(лаб)
                                        Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
import os


cur_dir = os.path.join('Урок 5. Практическое задание', 'task_6')
file_path_read = os.path.join(cur_dir, 'task_6_data.txt')
with open(file_path_read, 'r', encoding='utf-8') as f:
    data = f.readlines()
    new_list = [el.split() for el in data]
    new_dict = {}
    for el in new_list:
        sum_of_hours = 0
        label = ''
        for sub_el in el:
            if el.index(sub_el) == 0:
                label = sub_el
            else:
                new_el = sub_el.replace('(л)', '')\
                               .replace('(пр)', '')\
                               .replace('(лаб)', '')\
                               .replace('—', str(0))
                new_el = int(new_el)
                sum_of_hours += new_el
        new_dict[label] = sum_of_hours
    print(new_dict)
