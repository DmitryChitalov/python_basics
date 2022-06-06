"""
6)	Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                                        Физика:   30(л)   —   10(лаб)
                                        Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
subj_dict = {}
with open('subjects.txt', encoding='utf-8') as f_obj:
    for line in f_obj:
        norm_line = line.replace('(л)', '').replace('(пр)', '').replace('(лаб)', '').replace('\n', '')
        temp_list = norm_line.split(' ')
        sum_subj = 0
        for i in temp_list:
            if i.isnumeric():
                sum_subj += int(i)
        subj_dict[temp_list[0]] = sum_subj
print(subj_dict)
