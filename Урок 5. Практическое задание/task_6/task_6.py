"""
6)	Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                                        Физика:   30(л)   —   10(лаб)
                                        Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

lesson_dict = {}
with open("task_6.txt", encoding='utf-8') as les:
    for line in les:
        clear_line = line.replace("(л)", "").replace("(пр)", "").replace("(лаб)", "").replace(".", "")
        subject, lecture, practice, lab = clear_line.split()

        lect_int = 0
        practice_int = 0
        lab_int = 0
        if lecture != "-":
            lect_int = int(lecture)
        if practice != "-":
            practice_int = int(practice)
        if lab != "-":
            lab_int = int(lab)
        lesson_dict[subject] = lect_int + practice_int + lab_int
    print(f"{lesson_dict}")
    les.close()
