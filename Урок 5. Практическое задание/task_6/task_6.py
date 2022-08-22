"""
6)	Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный
предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их
количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                                        Физика:   30(л)   —   10(лаб)
                                        Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

file_name = "file.txt"
course_dict = {}
with open(file_name) as in_file:
    for s in in_file:
        s_args = list(s.split(" "))
        d_key = ''
        d_value = 0
        for arg in s_args:
            if arg.find(":") != -1:
                d_key = arg.rstrip(":")
            elif arg == '':
                pass
            else:
                try:
                    d_value += int(arg.strip("()лабпр.\n"))
                except ValueError:
                    pass
        course_dict.update({d_key: d_value})

print(course_dict)