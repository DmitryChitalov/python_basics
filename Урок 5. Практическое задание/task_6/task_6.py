"""
6)	Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                                        Физика:   30(л)   —   10(лаб)
                                        Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
result = {}
with open('curriculum.txt', 'r') as file:
    for line in file:
        subject = line.split(':')[0]
        program = line.split(':')[1]
        program = program.replace("(л)", "")
        program = program.replace("(пр)", "")
        program = program.replace("(лаб)", "")
        program = program.split()
        count_lessons = 0
        for el in program:
            try:
                count_lessons += int(eval(el))
            except:
                continue
        result.update({subject: count_lessons})

print(result)