"""
6)	Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                     Физика:   30(л)   —   10(лаб)
                     Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
subjects = {}
with open('some_lessons.txt', 'r', encoding='utf-8') as file:
    for line in file:
        divided_parts = line.split(":")
        subject = divided_parts[0].strip()
        lessons = divided_parts[1].strip().split()
        final_res = 0
        for lesson in lessons:
            if lesson.endswith("(л.)"):
                final_res += int(lesson[:-4])
            elif lesson.endswith("(пр.)"):
                final_res += int(lesson[:-5])
            elif lesson.endswith("(лаб.)"):
                final_res += int(lesson[:-6])
        subjects[subject] = final_res
print(subjects)
