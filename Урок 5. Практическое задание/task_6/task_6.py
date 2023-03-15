"""
6)	Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                                        Физика:   30(л)   —   10(лаб)
                                        Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
subj_list = {'Информатика': 170, 'Физика': 40, 'Физкультура': 30}
try:
    file_obj = open("task_5.txt", 'w')
    for subj, hours in subj_list.items():
        file_obj.write(subj + ': ' + str(hours) + "\n")
except IOError:
    print("Ошибка")
finally:
    file_obj.close()
with open("task_6.txt", "r") as file_obj:
    for line in file_obj:
        print(line, end="")

with open('task_6.txt', 'r') as file_obj:
    for line in file_obj:
        subject, lecture, practice, lab = line.split()
        subj[subject] = int(lecture) + int(practice) + int(lab)
    print(f'Общее количество часов по предмету - \n {subj}')