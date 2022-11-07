"""
6)	Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                                        Физика:   30(л)   —   10(лаб)
                                        Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
import re


def parse_subject(subj_str):
    parts = subj_str.split(":")
    subj_name = parts[0].strip()
    types_str = parts[1].strip()
    types_list = re.findall(r"((\d+)\(\w+\)|(-))", types_str)

    result = {"name": subj_name, "hrs": []}
    for val_str in types_list:
        val = 0 if val_str[2] == '-' else int(val_str[1])
        result["hrs"].append(val)
    return result


f_lines = []
try:
    with open("academic_subjects.txt", encoding="utf-8") as f_obj:
        f_lines = f_obj.readlines()
except IOError:
    print("Ошибка!")

subjects = {}
for line in f_lines:
    subject = parse_subject(line)
    subjects[subject["name"]] = sum(subject["hrs"])
