"""
6)	Необходимо создать (не программно) текстовый файл,
 где каждая строка описывает учебный предмет и наличие лекционных,
 практических и лабораторных занятий по этому предмету и их количество.
  Важно, чтобы для каждого предмета не обязательно были все типы занятий.
  Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
   Вывести словарь на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                                        Физика:   30(л)   —   10(лаб)
                                        Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

subj = {}
with open('for.hw.6_3.txt', 'r', encoding='UTF-8') as init_f:
    for line in init_f:
        subject, interprater = line.split(":")
        lecture, practice, lab = interprater.split("-")
        try:
            lecture_time, remains = lecture.split("(")
        except ValueError:
            lecture_time = 0
        try:
            practice_time, remains = practice.split("(")
        except ValueError:
            practice_time = 0
        try:
            lab_time, remains = lab.split("(")
        except ValueError:
            lab_time = 0
        subj[subject] = int(lecture_time) + int(practice_time) + int(lab_time)
    print(f'Общее количество часов по предмету - \n {subj}')
