"""
6)	Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                                        Физика:   30(л)   —   10(лаб)
                                        Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

import re

def get_lesson_counts(line):
    lesson_info = line.split(";")
    lesson_name = lesson_info[0]
    lesson_count = 0

    ndx = 1
    while ndx < len(lesson_info):
        count_info = re.sub(r"[^0-9]", "", lesson_info[ndx])
        if str.isdigit(count_info):
            lesson_count += int(count_info)
        
        ndx += 1
    
    return lesson_name, lesson_count

lessons = {}
with open("task6.csv", "r", encoding = "utf-8") as file:
    line = file.readline()
    while line != "":
        lesson_name, lesson_count = get_lesson_counts(line)
        lessons[lesson_name] = lesson_count
        line = file.readline()

print(lessons)