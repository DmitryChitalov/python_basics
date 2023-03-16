"""
6)	Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                                        Физика:   30(л)   —   10(лаб)
                                        Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""



abb = ['(л)', '(пр)', '(лаб)']
school_subjects = {}
try:
     with open("file_6.txt", 'r', encoding='utf-8') as file:
         subjects = file.readlines()
         for subject in subjects:
             summ = 0
             for data in subject.split():
                 for el in abb:
                     if el in data:
                         summ += int(data.replace(el, ''))
             school_subjects[subject.split()[0]] = summ
         print(school_subjects)
except IOError:
    print("Ошибка ввода-вывода!")
