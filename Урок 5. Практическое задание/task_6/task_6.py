"""
6)	Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                                        Физика:   30(л)   —   10(лаб)
                                        Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
import re

report = {}
with open("academic_subjects.txt", "r", encoding="UTF-8") as s_obj:
    f_text = s_obj.read()
    s_obj.seek(0)
    for row in s_obj:
        row_items = row.split(': ')
        hours = re.findall(r"\d+", row_items[1])
        report.update({row_items[0]: sum([int(i) for i in hours])})

print(f"Исходный файл:\n{f_text}\n")
print(f"Словарь:\n{report}")
