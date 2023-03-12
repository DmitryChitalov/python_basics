"""
6)	Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                                        Физика:   30(л)   —   10(лаб)
                                        Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""


filename = "subjects.txt"
subjects = {}

with open(filename, "r", encoding='utf-8') as f:
    for line in f:
        parts = line.split(":")
        subject = parts[0].strip()
        lessons = parts[1].strip().split()
        total = 0
        for lesson in lessons:
            if lesson.endswith("(л)"):
                total += int(lesson[:-3])
            elif lesson.endswith("(пр)"):
                total += int(lesson[:-4])
            elif lesson.endswith("(лаб)"):
                total += int(lesson[:-5])
        subjects[subject] = total

print(subjects)
