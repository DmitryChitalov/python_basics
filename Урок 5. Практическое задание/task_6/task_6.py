"""
6)	Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                                        Физика:   30(л)   —   10(лаб)
                                        Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
items = {}
with open("task_6.txt", "r") as my_f:
    for line in my_f:
        name, lesson, practice, lab = line.split()
        items[name] = int(lesson) + int(practice) + int(lab)

    print(f"Result {items}")

"""
Информатика: 60 100 40
Физика: 60 0 40
Физкультура: 60 10 0
Result {'Информатика:': 200, 'Физика:': 100, 'Физкультура:': 70}
"""